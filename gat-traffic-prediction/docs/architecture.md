# Architecture

This project isolates the **traffic prediction** function from downstream routing decisions.

- Input: road-segment graph snapshots with node-level traffic state at time `t`.
- Model: two-layer GAT regressor predicting travel time at `t + 5 minutes`.
- Output: per-road-segment travel-time estimates plus metadata for integration.
- Boundary: no route decision logic is implemented here.

Data flow:
1. Acquire or construct road network.
2. Build directed segment graph and stable segment mapping.
3. Generate synthetic or optional SUMO snapshots.
4. Train and evaluate GAT + baselines using scenario-aware splits.
5. Serve predictions through notebook demo and `Predictor` interface.
