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
    ### This Notebook contains an example that shows how to use the Camera_Calibration_API to calibrate using a chessboard pattern
    """)
    return


@app.cell
def _():
    import sys
    sys.path.append("../../")
    from camera_calibration import Camera_Calibration_API
    import glob
    import cv2
    import matplotlib.pyplot as plt
    # '%matplotlib inline' command supported automatically in marimo
    return Camera_Calibration_API, cv2, glob, plt


@app.cell
def _(Camera_Calibration_API):
    print(Camera_Calibration_API.__doc__)
    return


@app.cell
def _(glob):
    images_path_list = glob.glob("../example_images/chessboard/*.jpg")
    print(len(images_path_list))
    return (images_path_list,)


@app.cell
def _(cv2, images_path_list, plt):
    # visualize one of the calibration images
    test_img = cv2.imread(images_path_list[0],0)
    plt.figure(figsize=(8,8))
    plt.imshow(test_img,cmap="gray")
    plt.title("One of the calibration images")
    plt.show()
    print(test_img.shape)
    return


@app.cell
def _(Camera_Calibration_API):
    # initialize the constructor
    # optionally supply path to debug directory to save the visualized images.
    # if the given debug directory doesn't exists in the path it creates the given directory
    chessboard = Camera_Calibration_API(pattern_type="chessboard",
                                        pattern_rows=7,
                                        pattern_columns=6,
                                        distance_in_world_units = 10 #lets assume the each square is 10 in some world units
                                       )
    return (chessboard,)


@app.cell
def _(chessboard):
    print(chessboard.calibrate_camera.__doc__)
    return


@app.cell
def _(chessboard, images_path_list):
    # magic command not supported in marimo; please file an issue to add support
    # %%time
    Results = chessboard.calibrate_camera(images_path_list)
    return (Results,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The instance contains a useful instance variable called as calibration_df which contains all the details of the calibration for each image
    """)
    return


@app.cell
def _(chessboard):
    chessboard.calibration_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### you want to remove the images with high reprojection errors and recalibrate?

    As an example lets remove the images with reprojection error > 0.3 and recalibrate
    """)
    return


@app.cell
def _(chessboard):
    refined_images_paths = [img_path for i,img_path in enumerate(chessboard.calibration_df.image_names) if chessboard.calibration_df.reprojection_error[i] < 0.03]
    return (refined_images_paths,)


@app.cell
def _(Camera_Calibration_API):
    # create another instance
    refined_chessboard = Camera_Calibration_API(pattern_type="chessboard",
                                        pattern_rows=7,
                                        pattern_columns=6,
                                        distance_in_world_units = 10) #lets assume the each square is 10 in some world units
    return (refined_chessboard,)


@app.cell
def _(refined_chessboard, refined_images_paths):
    # pass this new list of image_paths
    refined_results = refined_chessboard.calibrate_camera(refined_images_paths)
    return (refined_results,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### The difference is not marginal in the above case. But this can give some improvements in calibration if many outliers are found
    """)
    return


@app.cell
def _(chessboard):
    print(chessboard.visualize_calibration_boards.__doc__)
    return


@app.cell
def _(refined_chessboard):
    refined_chessboard.visualize_calibration_boards(cam_width=10,cam_height=5)
    return


@app.cell
def _(Results):
    Results
    return


@app.cell
def _(refined_results):
    refined_results
    return


if __name__ == "__main__":
    app.run()
