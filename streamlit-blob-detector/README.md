# Streamlit Blob Detector

This project is a Streamlit application that allows users to detect blobs in images using customizable parameters. Users can adjust filters and tuning parameters through a user-friendly interface.

## Project Structure

```
streamlit-blob-detector
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   └── utils
│       └── blob_detector.py   # Contains the blob detection logic
├── requirements.txt          # Lists the project dependencies
└── README.md                 # Project documentation
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd streamlit-blob-detector
pip install -r requirements.txt
```

## Usage

To run the Streamlit application, execute the following command:

```bash
streamlit run src/app.py
```

Once the application is running, you can:

- Use sliders to adjust the parameters for blob detection.
- Turn filters on and off using checkboxes.
- Upload images to see the blob detection results in real-time.

## Dependencies

The project requires the following Python packages:

- Streamlit
- OpenCV (for image processing)
- NumPy (for numerical operations)

Make sure to install these packages using the `requirements.txt` file provided.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.