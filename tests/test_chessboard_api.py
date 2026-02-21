import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from camera_calibration import Camera_Calibration_API

def test_chessboard_api_doc():
    assert hasattr(Camera_Calibration_API, '__doc__')
    assert 'calibrate camera' in Camera_Calibration_API.__doc__.lower()

def test_chessboard_api_init():
    api = Camera_Calibration_API(
        pattern_type='chessboard',
        pattern_rows=7,
        pattern_columns=8,
        distance_in_world_units=1.0
    )
    assert api.pattern_type == 'chessboard'
    assert api.pattern_rows == 7
    assert api.pattern_columns == 8

def test_chessboard_api_methods():
    api = Camera_Calibration_API(
        pattern_type='chessboard',
        pattern_rows=7,
        pattern_columns=8,
        distance_in_world_units=1.0
    )
    # Check for method existence
    assert hasattr(api, 'pattern_type')
    assert hasattr(api, 'pattern_rows')
    assert hasattr(api, 'pattern_columns')
