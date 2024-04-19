import cv2
import face_recognition
from PIL import Image, ImageDraw
import os
import time

# Load and encode known faces
known_encodings = []
known_names = []
known_faces_dir = "known_face"

for filename in os.listdir(known_faces_dir):
    known_image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
    known_face_encodings = face_recognition.face_encodings(known_image, model="small")
    if len(known_face_encodings) > 0:
        known_face_encoding = known_face_encodings[0]
        known_encodings.append(known_face_encoding)
        known_names.append(os.path.splitext(filename)[0])
    else:
        print(f"No face found in {filename}")


# Start recording
record_start_time = time.time()
frames = []

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Encode the faces using FaceNet model
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations, model="facenet")

    # Loop through the face locations and encodings
    for face_location, face_encoding in zip(face_locations, face_encodings):
        top, right, bottom, left = face_location

        # Compare the face encoding with the known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)

        # Draw a rectangle around the face
        if True in matches:
            label = "Face matched!"
            color = (0, 255, 0)  # Green rectangle for a match
        else:
            label = "Unknown face"
            color = (0, 0, 255)  # Red rectangle for an unknown face

        # Draw the rectangle and label on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        cv2.putText(frame, label, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
video_capture.release()
cv2.destroyAllWindows()
