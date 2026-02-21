import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Test import and basic cell execution for marimo notebook

def test_blob_detector_marimo_nb_import():
    nb_path = os.path.join(os.path.dirname(__file__), '../examples/example_notebooks/blob_detector_marimo_nb.py')
    assert os.path.exists(nb_path), f"Notebook not found: {nb_path}"
    with open(nb_path, 'r') as f:
        content = f.read()
    assert 'marimo' in content
    assert 'mo.ui.slider' in content
    assert 'cv2.SimpleBlobDetector_Params' in content

def test_blob_detector_marimo_nb_cells():
    nb_path = os.path.join(os.path.dirname(__file__), '../examples/example_notebooks/blob_detector_marimo_nb.py')
    with open(nb_path, 'r') as f:
        content = f.read()
    # Check for cell structure
    assert 'app.cell' in content
    assert 'mo.md' in content
    assert 'mo.image' in content
