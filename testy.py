import face_recognition
from PIL import Image, ImageDraw

# Load the image
image = face_recognition.load_image_file("ObamaFamily.webp")

# Find faces in the image
face_locations = face_recognition.face_locations(image)

# Load and encode known faces
known_image = face_recognition.load_image_file("known_face/obama.jpeg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Create a PIL image object from the loaded image
pil_image = Image.fromarray(image)

# Create a drawing object
draw = ImageDraw.Draw(pil_image)

# Loop through the face locations
for face_location in face_locations:
    top, right, bottom, left = face_location

    # Encode the face
    face_encoding = face_recognition.face_encodings(image, [face_location])[0]

    # Compare the face encoding with the known encoding
    match = face_recognition.compare_faces([known_encoding], face_encoding)

    # Draw a rectangle around the face
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))  # Red rectangle

    # Add a label to indicate if the face matched or not
    if match[0]:
        label = "Face matched!"
    else:
        label = "Face did not match."
    draw.text((left, top - 20), label, fill=(0, 0, 255))  # Red text

# Display the image with the rectangles and labels
pil_image.show()