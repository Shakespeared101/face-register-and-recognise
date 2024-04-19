# %%
import face_recognition
import os

# %%
known_faces = []
known_names = []

# Directory containing images of known faces
known_faces_dir = "known_faces"

# Loop through each image file in the known_faces directory
for filename in os.listdir(known_faces_dir):
    image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
    encoding = face_recognition.face_encodings(image)[0]  # Assume there's only one face in each image
    known_faces.append(encoding)
    # Extract the name from the filename (assuming the filename is in the format "name.jpg")
    known_names.append(os.path.splitext(filename)[0])


# %%
unknown_image = face_recognition.load_image_file("family.jpeg")
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]


# %%
for i, known_face_encoding in enumerate(known_faces):
    # Compare the unknown face encoding with each known face encoding
    matches = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)
    
    # Check if the unknown face matches any of the known faces
    if matches[0]:
        print("The unknown face belongs to:", known_names[i])
        break
else:
    print("Unknown face")



