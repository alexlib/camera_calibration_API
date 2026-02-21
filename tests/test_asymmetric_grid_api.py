import sys
import os
import cv2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from camera_calibration import Camera_Calibration_API

def test_asymmetric_grid_api_init():
    api = Camera_Calibration_API(
        pattern_type='asymmetric_circles',
        pattern_rows=7,
        pattern_columns=8,
        distance_in_world_units=1.0
    )
    assert api.pattern_type == 'asymmetric_circles'
    assert api.pattern_rows == 7
    assert api.pattern_columns == 8

def test_asymmetric_grid_api_image():
    img_path = os.path.join(os.path.dirname(__file__), '../examples/example_images/asymmetric_grid/Image__2018-02-12__15-11-38.png')
    if os.path.exists(img_path):
        img = cv2.imread(img_path, 0)
        assert img is not None
        assert len(img.shape) == 2
        assert img.shape[0] > 0 and img.shape[1] > 0
