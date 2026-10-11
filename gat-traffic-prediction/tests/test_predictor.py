import numpy as np
import torch

from gat_traffic.predictor import Predictor


def test_predictor_checkpoint_and_shape(tmp_path):
    model = torch.nn.Linear(4, 1)
    ckpt = {
        "in_dim": 4,
        "model_state_dict": model.state_dict(),
        "feature_mean": [0.0, 0.0, 0.0, 0.0],
        "feature_std": [1.0, 1.0, 1.0, 1.0],
        "target_mean": 10.0,
        "target_std": 2.0,
        "model_version": "test-v1",
    }
    path = tmp_path / "model.pt"
    torch.save(ckpt, path)

    predictor = Predictor.from_checkpoint(path)
    preds = predictor.predict(
        snapshot_id=9,
        prediction_horizon_sec=300,
        road_segment_ids=["s1", "s2"],
        features=np.zeros((2, 4), dtype=np.float32),
    )

    assert len(preds) == 2
    assert preds[0].model_version == "test-v1"
    assert np.isfinite(preds[0].predicted_travel_time_sec)
