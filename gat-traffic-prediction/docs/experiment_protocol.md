# Experiment Protocol

1. Run Notebook 00 to inspect environment and dependencies.
2. Build graph and generate synthetic data (Notebooks 01-03).
3. Explore and validate data quality (Notebook 05).
4. Implement and verify model construction (Notebooks 06-07).
5. Train GAT and baselines with scenario-aware split (Notebook 08).
6. Evaluate by traffic regime and incidents (Notebook 09).
7. Inspect attention and run inference demo (Notebooks 10-11).

Split rule: scenario IDs are split into train/val/test so temporal neighbors from one scenario do not cross splits.
