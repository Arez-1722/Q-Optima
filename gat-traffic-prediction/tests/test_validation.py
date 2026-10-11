import pandas as pd
import pytest

from gat_traffic.validation import validate_snapshot_dataframe, scenario_split


def make_df():
    return pd.DataFrame(
        {
            "snapshot_id": [1, 1, 2],
            "scenario_id": [10, 10, 11],
            "simulation_run_id": [1, 1, 1],
            "timestamp_sec": [0, 0, 60],
            "road_segment_id": ["a", "b", "a"],
            "current_speed_kmh": [30.0, 31.0, 28.0],
            "current_density": [0.4, 0.5, 0.7],
            "queue_length": [1.0, 2.0, 4.0],
            "capacity_factor": [1.0, 1.0, 0.8],
            "closure_flag": [0, 0, 0],
            "target_travel_time_sec": [20.0, 21.0, 33.0],
            "prediction_horizon_sec": [300, 300, 300],
            "provenance": ["synthetic", "synthetic", "synthetic"],
        }
    )


def test_validate_snapshot_dataframe_ok():
    report = validate_snapshot_dataframe(make_df())
    assert report["num_snapshots"] == 2


def test_validate_snapshot_dataframe_missing():
    df = make_df().drop(columns=["provenance"])
    with pytest.raises(ValueError):
        validate_snapshot_dataframe(df)


def test_scenario_split_disjoint():
    train, val, test = scenario_split(range(10), seed=7)
    assert len(train & val) == 0
    assert len(train & test) == 0
    assert len(val & test) == 0
