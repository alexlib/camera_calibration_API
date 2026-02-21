from setuptools import setup, find_packages

setup(
    name="camera_calibration",
    version="0.1.1",
    description="Camera calibration tools and API based on the work of @Abhijit-2592",
    author="Alex Liberzon",
    packages=find_packages(),
    install_requires=[
        "marimo",
        "opencv-python-headless",
        "numpy",
        "pandas",
        "matplotlib"
    ],
    include_package_data=True,
    python_requires='>=3.11',
)
