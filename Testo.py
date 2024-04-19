import face_recognition
from PIL import Image, ImageDraw

# Load the image for recognition
image = face_recognition.load_image_file("ObamaFamily.webp")

# Find faces in the image
face_locations = face_recognition.face_locations(image)

if len(face_locations) == 0:
    print("No faces found in the image.")
else:
    # Encode the faces using FaceNet model
    face_encodings = face_recognition.face_encodings(image, face_locations, model="facenet")

    # Load and encode known faces
    known_encodings = []
    for known_image_path in ["known_face/obama.jpeg", "known_face/ObamaLeft.webp", "known_face/ObamaRight.jpeg", "known_face/ObamaRight2.jpeg"]:
        known_image = face_recognition.load_image_file(known_image_path)
        known_face_locations = face_recognition.face_locations(known_image)
        if len(known_face_locations) > 0:
            known_encoding = face_recognition.face_encodings(known_image, known_face_locations, model="facenet")[0]
            known_encodings.append(known_encoding)

    # Create a PIL image object from the loaded image
    pil_image = Image.fromarray(image)

    # Create a drawing object
    draw = ImageDraw.Draw(pil_image)

    # Loop through the face locations
    for face_location, face_encoding in zip(face_locations, face_encodings):
        top, right, bottom, left = face_location

        # Compare the face encoding with the known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)

        # Draw a rectangle around the face
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))  # Red rectangle

        # Add a label to indicate if the face matched or not
        if True in matches:
            label = "Face matched!"
        else:
            label = "Face did not match."
        draw.text((left, top - 20), label, fill=(0, 0, 255))  # Red text

    # Display the image with the rectangles and labels
    pil_image.show()
