import cv2
import face_recognition
import streamlit as st
import numpy as np
import os
import time
from PIL import Image
import dlib



# Load known faces and encodings
known_encodings = []
known_names = []
known_faces_dir = "known_faces"

for filename in os.listdir(known_faces_dir):
    if filename.endswith((".jpg", ".jpeg", ".png")):  # Check if the file has a valid image extension
        known_image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
        known_face_encodings = face_recognition.face_encodings(known_image)
        if len(known_face_encodings) > 0:
            known_face_encoding = known_face_encodings[0]
            known_encodings.append(known_face_encoding)
            known_names.append(os.path.splitext(filename)[0])
        else:
            st.warning(f"No face found in {filename}")


# Function to recognize faces
def recognize_faces(frame):
    # Convert the frame to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through the face locations and encodings
    for face_location, face_encoding in zip(face_locations, face_encodings):
        top, right, bottom, left = face_location

        # Compare the face encoding with the known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)

        # Draw a rectangle around the face
        if True in matches:
            label = known_names[matches.index(True)]
            color = (0, 255, 0)  # Green rectangle for a match
        else:
            label = "Unknown"
            color = (0, 0, 255)  # Red rectangle for an unknown face

        # Draw the rectangle and label on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, label, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    return frame

# Function to upload image and register face
def register_face(u_file):

    if u_file == 1:
        # Save the uploaded file
        with open(os.path.join(known_faces_dir, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Reload known faces and encodings
        known_encodings.clear()
        known_names.clear()
        for filename in os.listdir(known_faces_dir):
            known_image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
            known_face_encodings = face_recognition.face_encodings(known_image)
            if len(known_face_encodings) > 0:
                known_face_encoding = known_face_encodings[0]
                known_encodings.append(known_face_encoding)
                known_names.append(os.path.splitext(filename)[0])
            else:
                st.warning(f"No face found in {filename}")
        st.success("Face registered successfully!")
    else:
        st.warning("Upload an image to continue")

# Streamlit web application
def main():
    st.title("Face Recognition System")
    u_file = 0
    face_id = 0
    uploaded_file = st.file_uploader("Upload Image to Register Face", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        u_file = 1
    # Register face
    if st.button("Upload file to register face"):
        register_face(u_file)
    if st.button("Open webcam to register face"):
        st.write("Keep your face in position while the webcam initializes...")
        video_capture = cv2.VideoCapture(0)
        # Start monitoring
        start_time = time.time()
        while time.time() - start_time < 5:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
        # Display the resulting frame
        st.image(frame, channels="BGR")
        video_capture.release()
        cv2.destroyAllWindows()

        # Save captured frame as image
        filename = f"face_{int(time.time())}.jpg"
        filepath = os.path.join(known_faces_dir, filename)
        cv2.imwrite(filepath, frame)
        st.success("Face registered successfully!")
    # Start webcam and face recognition
    if st.button("Start Webcam and Face Recognition"):
        st.write("Please wait while the webcam initializes...")
        video_capture = cv2.VideoCapture(0)

        # Start monitoring
        start_time = time.time()
        while time.time() - start_time < 5:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            # Recognize faces
            frame = recognize_faces(frame)

            # Display the resulting frame
            st.image(frame, channels="BGR")

        # Release the webcam
        video_capture.release()

        # Display alert if no face matched
        if all(label == "Unknown" for label in known_names):
            st.warning("No known face detected!")

# Run the application
if __name__ == "__main__":
    main()
