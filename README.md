# 🛡️ DeepShield AI

### Deep Learning-Based Deepfake Video Detection System

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?style=for-the-badge&logo=pytorch)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📖 Overview

**DeepShield AI** is an advanced deepfake video detection platform that leverages deep learning techniques to identify manipulated and AI-generated videos.

By combining computer vision and sequential learning models, the system analyzes facial features and temporal inconsistencies within video frames to classify content as **Real** or **Fake** with high confidence.

Designed with a modern AI-powered web interface, DeepShield AI helps combat:

- Misinformation
- Digital Fraud
- Synthetic Media Threats
- Identity Manipulation

---

## 🚀 Features

- Deepfake Video Detection using Deep Learning
- Face Extraction and Analysis from Video Frames
- ResNeXt + LSTM Hybrid Architecture
- Real vs Fake Video Classification
- Confidence Score Generation
- Interactive AI Threat Assessment Dashboard
- Drag-and-Drop Video Upload Interface
- Real-Time Prediction Results
- Modern Responsive UI
- End-to-End Flask Web Application

---

## 🧠 How It Works

1. **Video Upload** – User uploads a video through the web interface.
2. **Frame Extraction** – Video frames are extracted using OpenCV.
3. **Face Detection** – Facial regions are detected and isolated.
4. **Feature Extraction** – ResNeXt extracts spatial features from facial frames.
5. **Temporal Analysis** – LSTM analyzes sequential frame patterns.
6. **Prediction** – The model classifies the video as Real or Fake and generates a confidence score.

---

## 🏗️ System Architecture

```text
Video Input
    │
    ▼
Frame Extraction (OpenCV)
    │
    ▼
Face Detection
    │
    ▼
ResNeXt Feature Extraction
    │
    ▼
LSTM Temporal Analysis
    │
    ▼
Classification Layer
    │
    ▼
Real / Fake Prediction
```

---

## 💻 Technology Stack

### Programming Languages

- Python
- JavaScript
- HTML5
- CSS3

### Backend

- Flask
- NumPy

### Deep Learning & Computer Vision

- PyTorch
- ResNeXt
- LSTM
- OpenCV
- Face Recognition

### Frontend

- Tailwind CSS
- JavaScript
- Glassmorphism UI Design

### Deployment

- GitHub
- Hugging Face Spaces

---

## 📂 Project Structure

```text
DeepShield-AI/
│
├── model/
│   └── df_model.pt
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── detect.html
│
├── uploads/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/SarasUgale/DeepShield-AI.git
cd DeepShield-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## 📊 Sample Prediction

```text
Prediction      : FAKE
Confidence Score: 99.96%
Threat Level    : Critical Risk
```

---


## 📸 Application Screenshots

<table>
<tr>
<td align="center">
<b>Home</b><br>
<img src="screenshots/home1.png" width="450">
</td>

<td align="center">
<b>Home</b><br>
<img src="screenshots/home2.png" width="450">
</td>
</tr>

<tr>
<td align="center">
<b>Home</b><br>
<img src="screenshots/home3.png" width="450">
</td>

<td align="center">
<b>Detect</b><br>
<img src="screenshots/upload.png" width="450">
</td>
</tr>
</table>
---

## Result pannel
<h2 align="center">Result pannel</h2>

<p align="center">
  <img src="screenshots/result-pannel.png" width="900">
</p>
## 🎯 Applications

- Media Verification
- Fake News Detection
- Social Media Monitoring
- Digital Forensics
- Cybersecurity
- Identity Protection
- Content Authenticity Verification
- Journalism & Fact Checking

---

## 🔮 Future Enhancements

- Explainable AI (XAI)
- Audio Deepfake Detection
- Deepfake Localization
- Batch Video Processing
- Cloud Deployment
- REST API Integration
- Real-Time Video Stream Analysis
- Multi-Modal Deepfake Detection

---

## 👨‍💻 Author

### Saras Ugale

**AI/ML Engineer | Deep Learning Enthusiast | Generative AI**

- GitHub: https://github.com/SarasUgale
- LinkedIn: https://www.linkedin.com/in/saras-ugale

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 📢 Share it with others

---

## 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project for educational and research purposes.

---

<div align="center">

### 🛡️ DeepShield AI
**Protecting Digital Trust with AI-Powered Deepfake Detection**

</div>
