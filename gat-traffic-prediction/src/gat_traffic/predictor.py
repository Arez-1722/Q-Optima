from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

import numpy as np
import torch

from .schema import PredictionRecord


class _FallbackLinear(torch.nn.Module):
    def __init__(self, in_dim: int):
        super().__init__()
        self.linear = torch.nn.Linear(in_dim, 1)

    def forward(self, x, edge_index=None):
        return self.linear(x)


@dataclass
class Predictor:
    model: torch.nn.Module
    feature_mean: np.ndarray
    feature_std: np.ndarray
    target_mean: float
    target_std: float
    model_version: str = "v0"
    device: str = "cpu"

    @classmethod
    def from_checkpoint(cls, checkpoint_path: str | Path) -> "Predictor":
        ckpt = torch.load(checkpoint_path, map_location="cpu")
        in_dim = int(ckpt.get("in_dim", 4))
        model = _FallbackLinear(in_dim)
        state = ckpt.get("model_state_dict", {})
        model.load_state_dict(state, strict=False)
        model.eval()
        return cls(
            model=model,
            feature_mean=np.array(ckpt.get("feature_mean", np.zeros(in_dim)), dtype=np.float32),
            feature_std=np.array(ckpt.get("feature_std", np.ones(in_dim)), dtype=np.float32),
            target_mean=float(ckpt.get("target_mean", 0.0)),
            target_std=float(ckpt.get("target_std", 1.0)),
            model_version=str(ckpt.get("model_version", "v0")),
            device=str(ckpt.get("device", "cpu")),
        )

    def predict(
        self,
        snapshot_id: int,
        prediction_horizon_sec: int,
        road_segment_ids: Iterable[str],
        features: np.ndarray,
    ) -> List[PredictionRecord]:
        x = np.asarray(features, dtype=np.float32)
        if x.ndim != 2:
            raise ValueError("features must be 2D")
        if x.shape[1] != self.feature_mean.shape[0]:
            raise ValueError("feature dimension mismatch")

        std = np.where(self.feature_std == 0, 1.0, self.feature_std)
        x_norm = (x - self.feature_mean) / std

        with torch.no_grad():
            pred_norm = self.model(torch.tensor(x_norm, dtype=torch.float32)).squeeze(-1).cpu().numpy()
        pred = pred_norm * self.target_std + self.target_mean

        records = []
        ids = list(road_segment_ids)
        if len(ids) != len(pred):
            raise ValueError("road_segment_ids length must match number of predictions")
        for rid, y in zip(ids, pred):
            records.append(
                PredictionRecord(
                    snapshot_id=int(snapshot_id),
                    prediction_horizon_sec=int(prediction_horizon_sec),
                    road_segment_id=str(rid),
                    predicted_travel_time_sec=float(max(y, 0.1)),
                    model_version=self.model_version,
                    is_valid=bool(np.isfinite(y)),
                )
            )
        return records
