from gat_traffic.schema import SnapshotRecord, PredictionRecord


def test_snapshot_record_fields():
    rec = SnapshotRecord(
        snapshot_id=1,
        scenario_id=2,
        simulation_run_id=3,
        timestamp_sec=10,
        road_segment_id="seg_1",
        current_speed_kmh=35.0,
        current_density=0.4,
        queue_length=3.0,
        capacity_factor=0.9,
        closure_flag=0,
        target_travel_time_sec=26.0,
        prediction_horizon_sec=300,
        provenance="synthetic",
    )
    assert rec.road_segment_id == "seg_1"


def test_prediction_record_fields():
    rec = PredictionRecord(1, 300, "seg_9", 40.0, "v0", True)
    assert rec.is_valid is True
