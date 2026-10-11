# Data Schema

Each row in the synthetic dataset represents one road-segment state within one snapshot.

Required fields:
- `snapshot_id`, `scenario_id`, `simulation_run_id`, `timestamp_sec`
- `road_segment_id`
- `current_speed_kmh`, `current_density`, `queue_length`, `capacity_factor`, `closure_flag`
- `target_travel_time_sec`, `prediction_horizon_sec`
- `provenance`

Graph topology is stored separately as edge list files and mapping tables.
