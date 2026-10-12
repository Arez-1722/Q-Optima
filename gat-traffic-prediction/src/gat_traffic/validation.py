from __future__ import annotations

from typing import Dict, Iterable, Tuple

import pandas as pd

REQUIRED_COLUMNS = {
    "snapshot_id",
    "scenario_id",
    "simulation_run_id",
    "timestamp_sec",
    "road_segment_id",
    "current_speed_kmh",
    "current_density",
    "queue_length",
    "capacity_factor",
    "closure_flag",
    "target_travel_time_sec",
    "prediction_horizon_sec",
    "provenance",
}


def validate_snapshot_dataframe(df: pd.DataFrame) -> Dict[str, object]:
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df.empty:
        raise ValueError("Snapshot dataframe is empty")
    if (df["prediction_horizon_sec"] <= 0).any():
        raise ValueError("prediction_horizon_sec must be positive")
    if (df["target_travel_time_sec"] <= 0).any():
        raise ValueError("target_travel_time_sec must be positive")
    if (df["closure_flag"] < 0).any():
        raise ValueError("closure_flag must be non-negative")

    null_counts = df[list(REQUIRED_COLUMNS)].isna().sum().to_dict()
    return {
        "num_rows": int(len(df)),
        "num_snapshots": int(df["snapshot_id"].nunique()),
        "num_scenarios": int(df["scenario_id"].nunique()),
        "null_counts": null_counts,
    }


def scenario_split(
    scenario_ids: Iterable[int],
    train_ratio: float = 0.7,
    val_ratio: float = 0.15,
    seed: int = 42,
) -> Tuple[set[int], set[int], set[int]]:
    if not 0 < train_ratio < 1:
        raise ValueError("train_ratio must be in (0,1)")
    if not 0 < val_ratio < 1:
        raise ValueError("val_ratio must be in (0,1)")
    if train_ratio + val_ratio >= 1:
        raise ValueError("train_ratio + val_ratio must be < 1")

    unique = sorted(set(int(x) for x in scenario_ids))
    if len(unique) < 3:
        raise ValueError("Need at least 3 unique scenarios for train/val/test split")

    shuffled = pd.Series(unique).sample(frac=1.0, random_state=seed).tolist()
    n = len(shuffled)
    n_train = max(1, int(n * train_ratio))
    n_val = max(1, int(n * val_ratio))
    n_test = n - n_train - n_val
    if n_test < 1:
        n_test = 1
        n_train = max(1, n_train - 1)

    train = set(shuffled[:n_train])
    val = set(shuffled[n_train:n_train + n_val])
    test = set(shuffled[n_train + n_val:])

    if train & val or train & test or val & test:
        raise RuntimeError("Scenario split overlap detected")
    return train, val, test
