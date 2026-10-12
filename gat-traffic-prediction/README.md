# gat-traffic-prediction

Notebook-first research workspace for GAT-based road-segment travel-time prediction.

## Goals
- Build a reproducible road-segment graph forecasting pipeline.
- Train a compact GAT model for `t + 5 min` travel-time prediction.
- Keep clear boundary between **prediction** and future routing decisions.

## Environment and installation
Preferred workflow uses `uv`; `pip` works too.

```bash
cd /home/runner/work/Q-Optima/Q-Optima/gat-traffic-prediction
uv venv
uv pip install -e .[notebooks,training,test]
```

Optional SUMO path:
```bash
uv pip install -e .[sumo]
```

## Notebook execution order
| Order | Notebook | Required |
|---|---|---|
| 00 | environment setup | Yes |
| 01 | road network acquisition/fallback | Yes |
| 02 | graph construction and visualization | Yes |
| 03 | synthetic traffic generation | Yes |
| 04 | SUMO data collection | Optional |
| 05 | dataset exploration | Yes |
| 06 | GAT first principles | Yes |
| 07 | GAT implementation | Yes |
| 08 | training and baselines | Yes |
| 09 | evaluation and error analysis | Yes |
| 10 | attention visualization | Yes |
| 11 | inference and agent integration | Yes |

## Data/artifact storage
- `data/synthetic/` generated synthetic snapshots and graph mapping
- `artifacts/checkpoints/` trained checkpoints
- `artifacts/figures/` plots
- `artifacts/metrics/` evaluation summaries

Large data/checkpoints are git-ignored by default.

## Reproducibility notes
- Fixed random seeds used in notebooks.
- Scenario-aware split prevents leakage.
- Normalization fit on training split only.
- Synthetic workflow does not require SUMO.

## Tests
```bash
pytest
```

## Known limitations
- Synthetic data is not a substitute for calibrated real Bangalore traffic.
- SUMO path requires local installation and network assets.
- Attention visualization is diagnostic, not causal proof.

## Remaining steps for real Bangalore/SUMO integration
1. Download and preprocess Bangalore OSM extract.
2. Build SUMO network and calibrated demand profiles.
3. Collect scenario metadata from simulation campaigns.
4. Re-train and compare against synthetic baseline under identical split protocol.
