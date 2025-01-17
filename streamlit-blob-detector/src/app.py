import streamlit as st
from streamlit_image_zoom import image_zoom
import numpy as np
import cv2
from PIL import Image

def main():

    st.title("Blob Detector")


    # Sidebar for filters
    st.sidebar.header("Filters")

    num_columns = st.sidebar.slider("Number of columns", 1, 20, value=8)
    num_rows = st.sidebar.slider("Number of rows", 1, 20, value=7)

    # use_filter = st.sidebar.checkbox("Use Filter", value=True)

    # Sliders for blob detection parameters
    st.sidebar.header("Blob Detection Parameters")   
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.filterByColor = st.sidebar.checkbox("Filter by color", value=True)
    params.minThreshold = st.sidebar.slider("Minimum Threshold", 0, 255, value=5)
    params.maxThreshold = st.sidebar.slider("Maximum Threshold", 0, 255, value=255)


    # Filter by Area.
    params.filterByArea = st.sidebar.checkbox("Filter by Area", value=True)
    params.minArea = st.sidebar.slider("Minimum Area", 0, 500, value=5)
    params.maxArea = st.sidebar.slider("Maximum Area", 0, 500, value=500)

    # Filter by Circularity
    params.filterByCircularity = st.sidebar.checkbox("Filter by cicrularity", value=True)
    params.minCircularity = st.sidebar.slider("Minimum circularity", 0., 1.0, step=0.1,value=0.1) 
    
    # Filter by Convexity
    params.filterByConvexity = st.sidebar.checkbox("Filter by convexity", value=True)
    params.minConvexity = st.sidebar.slider("Minimum Convexity", 0., 1.0, step=0.1,value=0.1)

    # Filter by Inertia
    params.filterByInertia = st.sidebar.checkbox("Filter by inertia", value=True)
    params.minInertiaRatio = st.sidebar.slider("Minimum InertiaRatio", 0., 1.0, step=0.01,value=0.01)


    # Create a detector with the parameters
    # OLD: detector = cv2.SimpleBlobDetector(params)
    detector = cv2.SimpleBlobDetector_create(params)


    # Load image (placeholder for actual image loading logic)
    image_file = st.file_uploader("Upload Image", type=["tiff","jpg", "jpeg", "png"])


    if image_file is not None:
        # Process the image with the blob detector
        # Detect blobs.

        # original_image = Image.open(image_file)
        # image = np.array(original_image).astype(np.uint8)

        image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), 0)

        keypoints = detector.detect(image)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
        # the size of the circle corresponds to the size of blob

        blank = np.zeros((1, 1))
        im_with_keypoints = cv2.drawKeypoints(image, keypoints, blank, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


        
        image_zoom(im_with_keypoints)
        
        found, corners = cv2.findCirclesGrid(image,(num_columns, num_rows),
                                                flags=cv2.CALIB_CB_SYMMETRIC_GRID,
                                                blobDetector=detector
                                                )
        st.write(f"Found: {found}")
        st.write(f"Corners: {corners}")
        vis = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        cv2.drawChessboardCorners(vis, (num_columns,num_rows), corners, found)
        image_zoom(vis)
        
        # st.write(f"Detected {len(found)} blobs.")

if __name__ == "__main__":
    main()