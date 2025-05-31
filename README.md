# 👁️Second Eye: Smart Assistive Face Recognition System

**Second Eye** is a smart, standalone assistive device designed for the visually impaired. It uses an **ESP32-CAM** to capture faces and a **Raspberry Pi** to locally recognize known people using face recognition and announce their names through offline text-to-speech — all without the need for internet.

---

## 💡 Project Overview

- 📸 ESP32-CAM captures a face and sends the image to the Raspberry Pi via HTTP POST.
- 🤖 Raspberry Pi runs a **Flask server** that:
  - Saves the captured image
  - Compares it with known faces using the `face_recognition` library
  - Announces the result using `pyttsx3` (offline TTS)
- 🔊 Automatically starts face recognition and TTS on boot.
- 🚫 No internet connection is required — works completely offline.

---

## 🔧 Features

- Real-time face capture from ESP32-CAM
- Automatic face recognition using `face_recognition`
- Offline TTS using `pyttsx3`
- Flask server auto-starts on Raspberry Pi boot
- Designed for blind or visually impaired users — no button press needed
- Standalone setup with Raspberry Pi (headless mode supported)

---

## 📦 Technologies Used

- ESP32-CAM (AI Thinker module)
- Raspberry Pi 4 Model B
- Python 3
- Flask (for HTTP server)
- numpy (Image array processing and data manipulation)
- face_recognition (based on dlib)
- pyttsx3 (offline text-to-speech)
- systemd (for Flask auto-start on boot)

---

## 🗂️ Project Structure
second-eye/
├── esp32-cam/
│   └── esp32-cam-face-capture.ino        # ESP32-CAM code (Arduino IDE)
│
├── raspberry-pi/
│   ├── face_server.py                    # Flask server handling upload and recognition
│   ├── known_faces/                      # Folder of labeled known face images
│   ├── uploads/                          # Incoming images from ESP32-CAM
│   ├── face_recognition_script.py        # Optional face recognition test script
│   └── flaskserver.service               # systemd service to autostart Flask on boot


---

## 🚀 How It Works

1. **Startup**: Raspberry Pi boots and automatically runs the Flask server.
2. **Capture**: ESP32-CAM captures a face and sends the image to Raspberry Pi.
3. **Recognition**:
   - Flask receives the image and saves it.
   - Compares the captured face with known faces.
4. **Response**:
   - If a match is found, the name is spoken using TTS.
   - If no match is found, it says “Unknown person.”

---

## 🛠️ Setup Instructions

### 1. ESP32-CAM (Arduino IDE)
- Upload the provided `.ino` sketch from `esp32-cam/`
- Set your Raspberry Pi's IP in the code
- Connect to Wi-Fi

### 2. Raspberry Pi Setup
- Install dependencies:
  
-sudo apt update && sudo apt upgrade -y
-sudo apt install build-essential cmake libopenblas-dev liblapack-dev libjpeg-dev libatlas-base-dev libavformat-dev libgtk2.0-dev python3-pyaudio espeak ffmpeg -y
**-pip install flask face_recognition numpy pyttsx3

---

### 📸Image Flow Diagram

       [👁️ ESP32-CAM]
              |
              | 📤 Captures face & sends image (HTTP POST)
              ↓
     [🌐 Flask Server on Raspberry Pi]
              |
              | 💾 Saves image
              ↓
   [🧐 face_recognition Library]
              |
     🔍 Compares with known faces
              ↓
 [✅ Match Found]     [❌ No Match]
      |                     |
      ↓                     ↓
 [🔊 Speaks name]     [🔊 Says "Unknown person"]
    (pyttsx3)              (pyttsx3)



### 🙋 Developed By
This project was developed by the team behind Second Eye under WireOT Private Ltd:

- AKHILESH K
- PRAJWAL D
- REETHU K
- SHARATH M D
