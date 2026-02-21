import marimo

__generated_with = "0.20.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### This Notebook shows how to use the Camera_Calibration_API to calibrate the camera using symmetrical circular grid pattern
    """)
    return


@app.cell
def _():
    import sys
    sys.path.append("../../")
    from camera_calibration import Camera_Calibration_API
    import glob
    import matplotlib.pyplot as plt
    # '%matplotlib inline' command supported automatically in marimo
    import os
    import cv2

    return Camera_Calibration_API, cv2, glob, plt


@app.cell
def _(cv2, plt):
    test_img = cv2.imread("/home/user/Downloads/Illmenau/KalibrierungA/Kalibrierung1a/00000030_00000000849B30C6.tiff",0)
    print(test_img.shape)
    plt.imshow(test_img,cmap="gray")
    plt.title("One of the calibration images")
    plt.show()
    return


@app.cell
def _(Camera_Calibration_API):
    symmetric_circles = Camera_Calibration_API(pattern_type="symmetric_circles",
                                              pattern_rows=7,
                                              pattern_columns=6,
                                              distance_in_world_units = 10,
                                              debug_dir=None)
    return (symmetric_circles,)


@app.cell
def _(glob, symmetric_circles):
    # magic command not supported in marimo; please file an issue to add support
    # %%time
    results = symmetric_circles.calibrate_camera(glob.glob("/home/user/Downloads/Illmenau/KalibrierungA/Kalibrierung1a/*.tiff"))
    return


@app.cell
def _(symmetric_circles):
    symmetric_circles.calibration_df
    return


@app.cell
def _(symmetric_circles):
    symmetric_circles.visualize_calibration_boards(20,10)
    return


if __name__ == "__main__":
    app.run()
