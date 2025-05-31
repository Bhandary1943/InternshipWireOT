import os
from flask import Flask, request
import face_recognition
from datetime import datetime
import numpy as np
import pyttsx3

# Setup
app = Flask(_name_)
UPLOAD_FOLDER = 'uploads'
KNOWN_FACES_FOLDER = 'known_faces'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Load known faces
known_encodings = []
known_names = []

for filename in os.listdir(KNOWN_FACES_FOLDER):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(KNOWN_FACES_FOLDER, filename)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            name = os.path.splitext(filename)[0]
            known_names.append(name)

# Function to speak text using TTS
def speak(text):
    print(f"??? Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

# Flask route to receive image
@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{now}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        # Save image
        with open(filepath, 'wb') as f:
            f.write(request.data)

        print(f"?? Image received and saved as {filename}")

        # Process image
        unknown_image = face_recognition.load_image_file(filepath)
        unknown_encodings = face_recognition.face_encodings(unknown_image)

        if not unknown_encodings:
            print("? No face found in image.")
            speak("No face found")
            return "No face found", 400

        unknown_encoding = unknown_encodings[0]
        distances = face_recognition.face_distance(known_encodings, unknown_encoding)
        print("?? Distances:", distances)

        best_match_index = np.argmin(distances)
        if distances[best_match_index] < 0.5:
            matched_name = known_names[best_match_index]
            print(f"? Match found: {matched_name}")
            speak(f"{matched_name} recognized")
            return f"Match found: {matched_name}", 200
        else:
            print("? No match found")
            speak("Match not found")
            return "No match found", 200

    except Exception as e:
        print("?? Error:", e)
        speak("Error occurred")
        return "Error", 500

# Run the Flask app
if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
