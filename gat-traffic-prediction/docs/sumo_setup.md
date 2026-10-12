# Optional SUMO Setup

SUMO is optional. If unavailable, use synthetic generation notebooks.

Windows (PowerShell) outline:
1. Install SUMO from official binaries.
2. Add `SUMO_HOME` and `%SUMO_HOME%/bin` to PATH.
3. Install Python client: `uv pip install traci`.
4. Verify with `sumo --version` and `python -c "import traci"`.

Notebook `04_sumo_data_collection.ipynb` exits gracefully when SUMO is missing.
