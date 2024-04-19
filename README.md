**Project Title: Face Recognition System with Streamlit**

**Overview:**
This project implements a simple face recognition system using the Streamlit framework in Python. It allows users to register known faces, capture faces from a webcam, and perform real-time face recognition.

**Key Features:**
Register known faces by uploading images or capturing from webcam.
Real-time face recognition using the webcam feed.
Alerting when an unknown face is detected or no face is detected within a specified timeframe.
Streamlit web interface for user interaction.

**Technologies Used:**
Python
OpenCV
Face Recognition Library
Streamlit

However, please note that the required `dlib` library is not included in the repository due to its size and build dependencies.

## Installation Instructions

### 1. Setting up a Virtual Environment (Optional but Recommended)
It's recommended to use a virtual environment to manage dependencies for this project. You can create a virtual environment using `venv` or `virtualenv`:

```bash
# Using venv
python3 -m venv myenv
source myenv/bin/activate

# Using virtualenv
virtualenv myenv
source myenv/bin/activate
```

### 2. Install dlib
The `dlib` library is a crucial dependency for this project. You can install it using the following steps:

#### Linux/macOS:
```bash
arch -arm64 pip3 install dlib
```

#### Windows:
```bash
pip install dlib
```

### 3. Install other Dependencies
Once the virtual environment is activated and `dlib` is installed, you can install the remaining dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Running the Application
After installing the dependencies, you can run the Streamlit application using the following command:

```bash
streamlit run StreamVidFace.py
```

Feel free to customize the installation instructions according to your specific requirements or environment setup.

**Contributors:**
* Shakthi B
* Aditya Sai SD
License:
This project is licensed under the MIT License.
