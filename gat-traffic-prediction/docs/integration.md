# Integration Contract

The future intelligent routing agent should consume model predictions as records:
- `snapshot_id`
- `prediction_horizon_sec`
- `road_segment_id`
- `predicted_travel_time_sec`
- `model_version`
- `is_valid`

The predictor does not select routes; it only estimates segment travel times.
Downstream components (shock detection, routing optimizer) should join on stable `road_segment_id`.
