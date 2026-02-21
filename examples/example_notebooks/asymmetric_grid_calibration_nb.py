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
    ### This Notebook shows how to use the Camera_Calibration_API to calibrate the camera using asymmetrical circular grid pattern
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
    test_img = cv2.imread("../example_images/asymmetric_grid/Image__2018-02-12__15-11-38.png",0)
    print(test_img.shape)
    plt.imshow(test_img,cmap="gray")
    plt.title("One of the calibration images")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### NOTE:

    * Kindly observe the above image. It contains 44 circles. The circles are placed in such a way that if distance between circles 1 and 3 is 10 units then the distance between circles 1 and 2 is 5 units. Thus use `distance_in_world_units` = 10 (Distance between adjacent circles in a row).

    * This pattern contains an additional setting called as `double_count_in_column` which is by default set to `True`. But in this case the double count is in rows (there are 11 circles in a row if you include the circles at half the distance between each row Hence the name double count). Be sure to change this to `False`
    """)
    return


@app.cell
def _(Camera_Calibration_API):
    asymmetric_circles = Camera_Calibration_API(pattern_type="asymmetric_circles",
                                              pattern_rows=11,
                                              pattern_columns=4,
                                              distance_in_world_units = 10,
                                              debug_dir=None)
    return (asymmetric_circles,)


@app.cell
def _(asymmetric_circles):
    asymmetric_circles.double_count_in_column = False # change this since in most cases the double count is in rows
    return


@app.cell
def _(asymmetric_circles, glob):
    results = asymmetric_circles.calibrate_camera(glob.glob("../example_images/asymmetric_grid/*.png"))
    return


@app.cell
def _(asymmetric_circles):
    asymmetric_circles.visualize_calibration_boards(20,10)
    return


@app.cell
def _(asymmetric_circles):
    asymmetric_circles.calibration_df
    return


if __name__ == "__main__":
    app.run()
