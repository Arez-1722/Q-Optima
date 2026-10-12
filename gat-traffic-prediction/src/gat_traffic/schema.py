from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SnapshotRecord:
    snapshot_id: int
    scenario_id: int
    simulation_run_id: int
    timestamp_sec: int
    road_segment_id: str
    current_speed_kmh: float
    current_density: float
    queue_length: float
    capacity_factor: float
    closure_flag: int
    target_travel_time_sec: float
    prediction_horizon_sec: int
    provenance: str


@dataclass(frozen=True)
class PredictionRecord:
    snapshot_id: int
    prediction_horizon_sec: int
    road_segment_id: str
    predicted_travel_time_sec: float
    model_version: str
    is_valid: bool
