def test_import_camera_calibration():
    try:
        __import__("camera_calibration")
    except ImportError as e:
        assert False, f"Import failed: {e}"
    else:
        assert True
