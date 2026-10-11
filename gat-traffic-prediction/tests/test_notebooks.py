from pathlib import Path
import nbformat

NOTEBOOKS = [
    "00_environment_setup.ipynb",
    "01_road_network_acquisition.ipynb",
    "02_graph_construction_and_visualization.ipynb",
    "03_synthetic_traffic_generation.ipynb",
    "04_sumo_data_collection.ipynb",
    "05_dataset_exploration.ipynb",
    "06_gat_from_first_principles.ipynb",
    "07_gat_implementation.ipynb",
    "08_training_and_baselines.ipynb",
    "09_evaluation_and_error_analysis.ipynb",
    "10_attention_visualization.ipynb",
    "11_inference_and_agent_integration.ipynb",
]


def test_notebook_files_exist_and_valid_json():
    root = Path(__file__).resolve().parents[1] / "notebooks"
    for name in NOTEBOOKS:
        nb_path = root / name
        assert nb_path.exists(), f"Missing notebook: {name}"
        nb = nbformat.read(nb_path, as_version=4)
        assert len(nb.cells) >= 6
        assert any(cell.cell_type == "markdown" for cell in nb.cells)
        assert any(cell.cell_type == "code" for cell in nb.cells)
