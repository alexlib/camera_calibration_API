import marimo
import numpy as np
import cv2
from PIL import Image

app = marimo.App()

@app.cell
def _():
    import marimo as mo
    mo.md("""
    # Blob Detector (Marimo UI)
    This notebook provides a UI for blob detection using OpenCV's SimpleBlobDetector.
    """)
    return mo

@app.cell
def _(mo):
    num_columns = mo.ui.slider(label="Number of columns", min=1, max=20, value=8)
    num_rows = mo.ui.slider(label="Number of rows", min=1, max=20, value=7)
    filter_by_color = mo.ui.checkbox(label="Filter by color", value=True)
    min_threshold = mo.ui.slider(label="Minimum Threshold", min=0, max=255, value=5)
    max_threshold = mo.ui.slider(label="Maximum Threshold", min=0, max=255, value=255)
    filter_by_area = mo.ui.checkbox(label="Filter by Area", value=True)
    min_area = mo.ui.slider(label="Minimum Area", min=0, max=500, value=5)
    max_area = mo.ui.slider(label="Maximum Area", min=0, max=500, value=500)
    filter_by_circularity = mo.ui.checkbox(label="Filter by circularity", value=True)
    min_circularity = mo.ui.slider(label="Minimum circularity", min=0.0, max=1.0, step=0.1, value=0.1)
    filter_by_convexity = mo.ui.checkbox(label="Filter by convexity", value=True)
    min_convexity = mo.ui.slider(label="Minimum Convexity", min=0.0, max=1.0, step=0.1, value=0.1)
    filter_by_inertia = mo.ui.checkbox(label="Filter by inertia", value=True)
    min_inertia_ratio = mo.ui.slider(label="Minimum InertiaRatio", min=0.0, max=1.0, step=0.01, value=0.01)
    image_upload = mo.ui.file(label="Upload Image", accept=[".tiff", ".jpg", ".jpeg", ".png"])
    return {
        "num_columns": num_columns,
        "num_rows": num_rows,
        "filter_by_color": filter_by_color,
        "min_threshold": min_threshold,
        "max_threshold": max_threshold,
        "filter_by_area": filter_by_area,
        "min_area": min_area,
        "max_area": max_area,
        "filter_by_circularity": filter_by_circularity,
        "min_circularity": min_circularity,
        "filter_by_convexity": filter_by_convexity,
        "min_convexity": min_convexity,
        "filter_by_inertia": filter_by_inertia,
        "min_inertia_ratio": min_inertia_ratio,
        "image_upload": image_upload
    }

@app.cell
def _(mo, params):
    mo.md("""
    ## Blob Detection Parameters
    Adjust the sliders and checkboxes to configure blob detection.
    """)
    return

@app.cell
def _(params):
    import cv2
    import numpy as np
    from PIL import Image
    image = None
    if params["image_upload"].value is not None:
        file_bytes = params["image_upload"].value.read()
        image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), 0)
    return image

@app.cell
def _(mo, params, image):
    if image is None:
        mo.md("Upload an image to begin blob detection.")
        return
    params_cv = cv2.SimpleBlobDetector_Params()
    params_cv.filterByColor = params["filter_by_color"].value
    params_cv.minThreshold = params["min_threshold"].value
    params_cv.maxThreshold = params["max_threshold"].value
    params_cv.filterByArea = params["filter_by_area"].value
    params_cv.minArea = params["min_area"].value
    params_cv.maxArea = params["max_area"].value
    params_cv.filterByCircularity = params["filter_by_circularity"].value
    params_cv.minCircularity = params["min_circularity"].value
    params_cv.filterByConvexity = params["filter_by_convexity"].value
    params_cv.minConvexity = params["min_convexity"].value
    params_cv.filterByInertia = params["filter_by_inertia"].value
    params_cv.minInertiaRatio = params["min_inertia_ratio"].value
    detector = cv2.SimpleBlobDetector_create(params_cv)
    keypoints = detector.detect(image)
    blank = np.zeros((1, 1))
    im_with_keypoints = cv2.drawKeypoints(image, keypoints, blank, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    mo.image(im_with_keypoints, format="png")
    found, corners = cv2.findCirclesGrid(image, (params["num_columns"].value, params["num_rows"].value), flags=cv2.CALIB_CB_SYMMETRIC_GRID, blobDetector=detector)
    mo.md(f"**Found:** {found}")
    mo.md(f"**Corners:** {corners}")
    vis = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if corners is not None:
        cv2.drawChessboardCorners(vis, (params["num_columns"].value, params["num_rows"].value), corners, found)
    mo.image(vis, format="png")
    return
