import sys
import os
import cv2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from camera_calibration import Camera_Calibration_API

def test_symmetric_grid_api_init():
    api = Camera_Calibration_API(
        pattern_type='symmetric_circles',
        pattern_rows=7,
        pattern_columns=8,
        distance_in_world_units=1.0
    )
    assert api.pattern_type == 'symmetric_circles'
    assert api.pattern_rows == 7
    assert api.pattern_columns == 8

def test_symmetric_grid_api_image():
    img_path = os.path.join(os.path.dirname(__file__), '../examples/example_images/symmetric_grid/00000030_00000000849B30C6.tiff')
    if os.path.exists(img_path):
        img = cv2.imread(img_path, 0)
        assert img is not None
        assert len(img.shape) == 2
        assert img.shape[0] > 0 and img.shape[1] > 0
