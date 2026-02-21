import marimo

__generated_with = "0.20.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import glob
    import matplotlib.pyplot as plt

    # '%matplotlib widget' command supported automatically in marimo
    import os, sys
    import cv2
    from camera_calibration import Camera_Calibration_API

    return Camera_Calibration_API, cv2, glob, mo, os, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### This Notebook shows how to use the Camera_Calibration_API to calibrate the camera using symmetrical circular grid pattern
    """)
    return


@app.cell
def _():
    # image_path = "/home/user/Downloads/Illmenau/KalibrierungA/Kalibrierung1a/00000009_00000000848D3231.tiff"
    image_path = "/home/user/Downloads/Illmenau/KalibrierungA/Kalibrierung1a/00000030_00000000849B30C6.tiff"
    return (image_path,)


@app.cell
def _(cv2, image_path, plt):
    test_img = cv2.imread(image_path, 0)
    print(test_img.shape)
    plt.imshow(test_img, cmap="gray")
    plt.title("One of the calibration images")
    # plt.show()
    return (test_img,)


@app.cell
def _(cv2, plt, test_img):
    import numpy as np

    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # # Change thresholds
    # params.filterByColor = False #True
    # params.minThreshold = 50
    # params.maxThreshold = 250


    # # Filter by Area.
    # params.filterByArea = True
    # params.minArea = 10

    # # Filter by Circularity
    # params.filterByCircularity = True
    # params.minCircularity = 0.1

    # # Filter by Convexity
    # params.filterByConvexity = True
    # params.minConvexity = 0.2

    # # Filter by Inertia
    # params.filterByInertia = True
    # params.minInertiaRatio = 0.01

    # THIS IS THE KEY:
    params.filterByColor = False

    # Ensure other filters are set so it doesn't pick up noise
    params.filterByArea = True
    params.minArea = 50
    params.filterByCircularity = True
    params.minCircularity = 0.7  # Adjust based on how round they are

    # Create a detector with the parameters
    # OLD: detector = cv2.SimpleBlobDetector(params)
    detector = cv2.SimpleBlobDetector_create(params)


    # Detect blobs.
    keypoints = detector.detect(test_img)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob

    blank = np.zeros((1, 1))
    im_with_keypoints = cv2.drawKeypoints(
        test_img,
        keypoints,
        blank,
        (255, 0, 0),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    )

    # Show blobs
    # plt.figure()
    plt.figure(figsize=(10, 10))

    # Displaying the image
    # plt.subplot(121)
    # plt.title('Original')
    # plt.imshow(test_img, cmap='gray')

    # plt.subplot(122)
    # plt.title('Blobs')
    plt.imshow(im_with_keypoints)
    return detector, np


@app.cell
def _(cv2, detector, plt, test_img):
    found, corners = cv2.findCirclesGrid(
        test_img, (6, 7), flags=cv2.CALIB_CB_SYMMETRIC_GRID, blobDetector=detector
    )
    vis = cv2.cvtColor(test_img, cv2.COLOR_GRAY2BGR)
    cv2.drawChessboardCorners(vis, (6, 7), corners, found)
    plt.figure(figsize=(8, 8))
    plt.imshow(vis)
    # plt.show()
    return


@app.cell
def _():
    # # import cv2
    # # import numpy as np

    # # def find_whiteboard(image_path):
    #     # Load the image
    # image = cv2.imread("/home/user/Downloads/Illmenau/KalibrierungA/Kalibrierung1a/00000030_00000000849B30C6.tiff")
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # # Preprocessing: Gaussian Blur and Thresholding
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # # Find contours of the dark dots
    # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # # Plot contours
    # plt.figure(figsize=(10, 10))
    # plt.imshow(image, cmap='gray')
    # for cnt in contours:
    #     plt.plot(cnt[:, 0, 0], cnt[:, 0, 1], 'r-', linewidth=2)
    # plt.title('Contours')
    # plt.show()

    # # Approximate the grid by sorting the dots spatially
    # dot_centers = []
    # for cnt in contours:
    #     M = cv2.moments(cnt)
    #     if M['m00'] != 0:
    #         cx = int(M['m10'] / M['m00'])  # x-coordinate of the center
    #         cy = int(M['m01'] / M['m00'])  # y-coordinate of the center
    #         dot_centers.append((cx, cy))

    # # Sort centers into a grid (7 rows x 8 columns)
    # dot_centers = np.array(dot_centers)
    # dot_centers = dot_centers[np.argsort(dot_centers[:, 1])]  # Sort by y-coordinate first (rows)

    # plt.figure()
    # plt.plot(dot_centers[:, 0], dot_centers[:, 1], 'ro')
    # plt.show()
    return


@app.cell
def _():
    # grid = []
    # for i in range(7):  # 7 rows
    #     row = dot_centers[i * 8:(i + 1) * 8]  # 8 columns per row
    #     row = row[np.argsort(row[:, 0])]  # Sort each row by x-coordinate
    #     grid.append(row)
    # grid = np.array(grid)

    # # Detect L-shaped dots
    # L_dots = []
    # for cnt in contours:
    #     # Create a mask for the current contour
    #     mask = np.zeros_like(thresh)
    #     cv2.drawContours(mask, [cnt], -1, 255, -1)

    #     # Check for white regions inside the dark dot
    #     white_inside = cv2.bitwise_and(thresh, thresh, mask=mask)
    #     white_contours, _ = cv2.findContours(white_inside, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #     if len(white_contours) > 0:  # If there's a white region inside the dark dot
    #         L_dots.append(cnt)

    # # Draw results
    # output = image.copy()
    # cv2.drawContours(output, contours, -1, (0, 255, 0), 2)  # Green for regular dots
    # cv2.drawContours(output, L_dots, -1, (0, 0, 255), 2)  # Red for L-shaped dots

    # # Draw grid or bounding box around the whiteboard
    # x, y, w, h = cv2.boundingRect(np.vstack(contours))
    # cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle

    # # Display results
    # plt.figure()
    # plt.imshow(output)
    # plt.title('Output')
    # plt.show()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Call the function with the image path
    # find_whiteboard("/home/user/Downloads/2021_03_31_Data_set/Calibration/B00009_a.tiff")
    return


@app.cell
def _(Camera_Calibration_API, detector, os):
    os.makedirs("./debug_dir", exist_ok=True)
    symmetric_circles = Camera_Calibration_API(
        pattern_type="symmetric_circles",
        pattern_rows=7,
        pattern_columns=6,
        distance_in_world_units=120,
        debug_dir="./debug_dir",
        blobDetector=detector,
    )
    return (symmetric_circles,)


@app.cell
def _(glob, image_path, symmetric_circles):
    # magic command not supported in marimo; please file an issue to add support
    # %%time
    results = symmetric_circles.calibrate_camera(
        glob.glob(
            "/home/user/Downloads/Illmenau/KalibrierungA/Kalibrierung1a/*.tiff"
        ),
        origin_image_filename=image_path,
    )
    return


@app.cell
def _(symmetric_circles):
    symmetric_circles.calibration_df
    return


@app.cell
def _(symmetric_circles):
    symmetric_circles.visualize_calibration_boards(20, 10)
    return


@app.cell
def _(symmetric_circles):
    # Find the row where the image name contains '0000030'
    target_row = symmetric_circles.calibration_df[
        symmetric_circles.calibration_df["image_names"].str.contains("0000030")
    ]
    target_row
    return (target_row,)


@app.cell
def _(cv2, mo, target_row):
    import math
    # import numpy as np # Already imported

    # Define pixel size (mm/pixel) - adjust based on your specific sensor specs
    pixel_size = 0.005

    if len(target_row) > 0:
        # 1. Extract rvec and tvec from the target_row
        # target_row is a DataFrame, so we access the values of the first (and likely only) row
        rvec_val = target_row["rvecs"].values[0]
        tvec_val = target_row["tvecs"].values[0]

        # 2. Compute Rotation Matrix R using Rodrigues
        R_matrix, _ = cv2.Rodrigues(rvec_val)

        # 3. Compute Camera Position in OpenCV World Coordinates
        # Formula: C = -R^T * t
        camera_pos_cv = -R_matrix.T @ tvec_val
    
        # 4. Convert to OpenPTV Coordinate System
        # OpenCV: X right, Y down, Z into board (assuming board is at z=0)
        # OpenPTV: X right, Y up, Z towards camera (out of board)
        # Transformation: X -> X, Y -> -Y, Z -> -Z
    
        # Transform Position
        camera_pos_optv = camera_pos_cv.copy()
        camera_pos_optv[1] = -camera_pos_cv[1] # Flip Y
        camera_pos_optv[2] = -camera_pos_cv[2] # Flip Z
    
        # Transform Rotation Matrix
        # We are negating the Y and Z axes of the World Frame.
        # This corresponds to negating the 2nd and 3rd columns of the Rotation Matrix.
        R_optv = R_matrix.copy()
        R_optv[:, 1] = -R_matrix[:, 1]
        R_optv[:, 2] = -R_matrix[:, 2]

        # 5. Compute Euler Angles (Phi, Omega, Kappa)
        # Note: These formulas depend on the specific rotation order conventions of OpenPTV.
        # Assuming the standard photogrammetric rotation matrix structure.
    
        phi = math.asin(R_optv[0, 2])
        omega = math.atan2(-R_optv[1, 2], R_optv[2, 2])
        kappa = math.atan2(-R_optv[0, 1], R_optv[0, 0])
    
        # Convert to degrees for readability
        phi_deg = math.degrees(phi)
        omega_deg = math.degrees(omega)
        kappa_deg = math.degrees(kappa)

        display_output = mo.md(f"""
        ### Camera Position and Orientation (OpenPTV)
    
        **Position (World Coordinates):**
        - X: {camera_pos_optv[0][0]:.4f}
        - Y: {camera_pos_optv[1][0]:.4f}
        - Z: {camera_pos_optv[2][0]:.4f}
    
        **Orientation (Radians):**
        - Phi: {phi:.4f}
        - Omega: {omega:.4f}
        - Kappa: {kappa:.4f}

        **Orientation (Degrees):**
        - Phi: {phi_deg:.4f}
        - Omega: {omega_deg:.4f}
        - Kappa: {kappa_deg:.4f}
        """)
    else:
        display_output = mo.md("Target row not found. Please check if the image name matches.")

    display_output
    return


@app.cell
def _(symmetric_circles):
    symmetric_circles.calibration_df.to_csv("./calibration_results_cam0.csv", index=False)
    return


@app.cell
def _(np, plt, target_row):
    # Extract the object points from the dataframe row
    # Assuming the format is compatible with OpenCV (N, 3) or (N, 1, 3)
    obj_pts_raw = target_row['obj_points'].values[0]
    obj_pts_arr = np.array(obj_pts_raw)

    # Squeeze dimensions if necessary (e.g. from (N, 1, 3) to (N, 3))
    if obj_pts_arr.ndim == 3:
        obj_pts_arr = obj_pts_arr.squeeze()
    
    # Create 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot
    ax.scatter(obj_pts_arr[:, 0], obj_pts_arr[:, 1], obj_pts_arr[:, 2], c='blue', marker='o')

    # Add labels and title
    ax.set_xlabel('X World')
    ax.set_ylabel('Y World')
    ax.set_zlabel('Z World')
    ax.set_title('3D Object Points (Calibration Pattern)')

    # Attempt to set aspect ratio to be roughly equal to see the grid structure correctly
    # (Matplotlib 3D auto-scaling can sometimes distort geometries)
    all_coords = obj_pts_arr.flatten()
    min_limit = np.min(all_coords)
    max_limit = np.max(all_coords)
    ax.set_xlim([np.min(obj_pts_arr[:,0]), np.max(obj_pts_arr[:,0])])
    ax.set_ylim([np.min(obj_pts_arr[:,1]), np.max(obj_pts_arr[:,1])])
    ax.set_zlim([np.min(obj_pts_arr[:,2]) - 10, np.max(obj_pts_arr[:,2]) + 10]) # Give Z some range even if flat

    # User requested view: Z towards us, X to right, Y upwards.
    # Standard Matplotlib 3D:
    #   Z is "Up".
    #   X/Y are on "floor".
    # To make Z point "towards us" (out of screen), we look from "top".
    #   This is elev=90.
    #   At elev=90, X is Horizontal, Y is Vertical by default?
    #   Let's check. usually at elev=90, azim=-90, X is right, Y is up.
    # ax.view_init(elev=90, azim=-90)

    plt.gca()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
