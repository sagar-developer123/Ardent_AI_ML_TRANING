# 🎭 Real-Time Facial Emotion Detection

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-Keras-orange?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/Deep%20Learning-CNN-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
</p>

<p align="center">
  A real-time facial emotion recognition system powered by a Convolutional Neural Network (CNN) and OpenCV — capable of detecting human emotions directly from a live webcam feed.
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Demo](#-demo)
- [Emotions Detected](#-emotions-detected)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Architecture](#-model-architecture)
- [How It Works](#-how-it-works)
- [Connect](#-connect)

---

## 🧠 Overview

This project implements a **real-time emotion detection pipeline** using:

- **OpenCV** with Haar Cascade Classifier for fast and efficient face detection
- A pre-trained **Keras/TensorFlow CNN model** (`emotion_model.hdf5`) for emotion classification
- Live video capture via webcam with bounding box and emotion label overlay

The system detects faces in each video frame, preprocesses the face region, and classifies it into one of several emotion categories — all in real time.

---

## 🎬 Demo

> Webcam feed → Face Detection → Emotion Classification → Live Label Overlay

<img width="429" height="577" alt="image" src="https://github.com/user-attachments/assets/d287c804-5310-46bc-af0d-8e7327a3c340" />

## 😄 Emotions Detected

| Label      | Emoji |
|------------|-------|
| Angry      | 😠    |
| Disgusted  | 🤢    |
| Fearful    | 😨    |
| Happy      | 😊    |
| Neutral    | 😐    |
| Sad        | 😢    |
| Surprised  | 😲    |

---

## 🛠️ Tech Stack

| Technology      | Purpose                              |
|-----------------|--------------------------------------|
| Python 3.8+     | Core programming language            |
| OpenCV          | Face detection & video capture       |
| TensorFlow/Keras| Deep learning model inference        |
| NumPy           | Array manipulation & preprocessing   |
| Haar Cascade    | Lightweight frontal face detector    |

---

## 📁 Project Structure

```
📦 emotion-detection/
├── emotion_detection.py              # Main script — run this to start
├── emotion_model.hdf5                # Pre-trained CNN model weights
├── haarcascade_frontalface_default.xml  # OpenCV face detector
└── README.md
```

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/sagar-developer123/emotion-detection.git
cd emotion-detection
```

**2. Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install tensorflow opencv-python numpy
```

> **Note:** If you face issues with TensorFlow, try `pip install tensorflow-cpu` for a lighter installation.

---

## ▶️ Usage

Run the main script to start real-time detection:

```bash
python emotion_detection.py
```

- Your webcam will activate automatically.
- Detected faces are highlighted with a **bounding box**.
- The predicted **emotion label** and confidence are displayed above each face.
- Press **`q`** to quit the application.

---

## 🏗️ Model Architecture

The emotion classifier is a **Convolutional Neural Network (CNN)** trained on grayscale facial images (48×48 pixels). The model (`emotion_model.hdf5`) was trained on the **FER-2013 dataset** and saved in Keras HDF5 format.

**Typical architecture:**
```
Input (48×48×1 grayscale)
    ↓
Conv2D + BatchNorm + ReLU
    ↓
Conv2D + BatchNorm + ReLU + MaxPool + Dropout
    ↓
Conv2D + BatchNorm + ReLU + MaxPool + Dropout
    ↓
Flatten → Dense (256) → Dropout
    ↓
Dense (7) + Softmax → Emotion Class
```

---

## 🔍 How It Works

1. **Frame Capture** — OpenCV reads frames from the webcam in real time.
2. **Face Detection** — The Haar Cascade classifier locates face regions within each frame.
3. **Preprocessing** — Detected face ROI is converted to grayscale, resized to 48×48, and normalized.
4. **Emotion Prediction** — The preprocessed image is fed into the CNN model, which outputs a probability distribution across 7 emotion classes.
5. **Visualization** — The top predicted emotion and bounding box are drawn onto the frame and displayed.

---

## 🤝 Connect

<p>
  <a href="https://www.linkedin.com/in/sagar-ghorai-3970123b2/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Sagar%20Ghorai-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://github.com/sagar-developer123" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-sagar--developer123-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute with attribution.

---

<p align="center">Made with ❤️ by <a href="https://github.com/sagar-developer123">Sagar Ghorai</a></p>
