import os
import requests

MODEL_PATH = "model/model.pt"

if not os.path.exists(MODEL_PATH):
    os.makedirs("model", exist_ok=True)

    url = "https://huggingface.co/Saras1341/deepfake-model/blob/main/df_model.pt"
    r = requests.get(url)

    with open(MODEL_PATH, "wb") as f:
        f.write(r.content)

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import torch
from torch import nn
from torchvision import models, transforms
import numpy as np
import cv2
import urllib.request
import warnings
warnings.filterwarnings("ignore")

UPLOAD_FOLDER = 'Celeb-DF-v2'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, template_folder="templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ── DNN face detector setup ──────────────────────────────────────────────────
# Uses OpenCV's ResNet-SSD face detector — significantly more accurate than
# Haar Cascade and behaviorally closest to face_recognition's HOG detector.
MODEL_DIR = "model"
PROTO_PATH = os.path.join(MODEL_DIR, "deploy.prototxt")
WEIGHTS_PATH = os.path.join(MODEL_DIR, "res10_300x300_ssd_iter_140000.caffemodel")

PROTO_URL = (
    "https://raw.githubusercontent.com/opencv/opencv/master/"
    "samples/dnn/face_detector/deploy.prototxt"
)
WEIGHTS_URL = (
    "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/"
    "res10_300x300_ssd_iter_140000.caffemodel"
)

os.makedirs(MODEL_DIR, exist_ok=True)

if not os.path.exists(PROTO_PATH):
    print("Downloading deploy.prototxt ...")
    urllib.request.urlretrieve(PROTO_URL, PROTO_PATH)

if not os.path.exists(WEIGHTS_PATH):
    print("Downloading face detector weights ...")
    urllib.request.urlretrieve(WEIGHTS_URL, WEIGHTS_PATH)

face_net = cv2.dnn.readNetFromCaffe(PROTO_PATH, WEIGHTS_PATH)
CONFIDENCE_THRESHOLD = 0.5   # only accept detections above 50% confidence
# ─────────────────────────────────────────────────────────────────────────────


def detect_face_dnn(frame):
    """
    Returns (top, right, bottom, left) of the most confident face,
    exactly matching the tuple format that face_recognition returned.
    Returns None if no face is found.
    """
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0)
    )
    face_net.setInput(blob)
    detections = face_net.forward()

    best = None
    best_conf = CONFIDENCE_THRESHOLD

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > best_conf:
            best_conf = confidence
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            x1, y1, x2, y2 = box.astype(int)
            # Clamp to frame boundaries
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)
            # Return as (top, right, bottom, left) — same as face_recognition
            best = (y1, x2, y2, x1)

    return best


class Model(nn.Module):
    def __init__(self, num_classes, latent_dim=2048, lstm_layers=1, hidden_dim=2048, bidirectional=False):
        super(Model, self).__init__()
        model = models.resnext50_32x4d(pretrained=True)
        self.model = nn.Sequential(*list(model.children())[:-2])
        self.lstm = nn.LSTM(latent_dim, hidden_dim, lstm_layers, bidirectional)
        self.relu = nn.LeakyReLU()
        self.dp = nn.Dropout(0.4)
        self.linear1 = nn.Linear(2048, num_classes)
        self.avgpool = nn.AdaptiveAvgPool2d(1)

    def forward(self, x):
        batch_size, seq_length, c, h, w = x.shape
        x = x.view(batch_size * seq_length, c, h, w)
        fmap = self.model(x)
        x = self.avgpool(fmap)
        x = x.view(batch_size, seq_length, 2048)
        x_lstm, _ = self.lstm(x, None)
        return fmap, self.dp(self.linear1(x_lstm[:, -1, :]))


sm = nn.Softmax(dim=1)


class ValidationDataset(torch.utils.data.Dataset):
    def __init__(self, video_names, sequence_length=60, transform=None):
        self.video_names = video_names
        self.transform = transform
        self.count = sequence_length

    def __len__(self):
        return len(self.video_names)

    def __getitem__(self, idx):
        video_path = self.video_names[idx]
        frames = []

        for frame in self.frame_extract(video_path):
            # Detect face — returns (top, right, bottom, left) like face_recognition
            face = detect_face_dnn(frame)

            if face is not None:
                top, right, bottom, left = face
                frame = frame[top:bottom, left:right, :]
            # else: use full frame (same as original except IndexError: pass)

            if self.transform:
                frame = self.transform(frame)

            frames.append(frame)

            if len(frames) == self.count:
                break

        frames = torch.stack(frames)
        frames = frames[:self.count]
        return frames.unsqueeze(0)

    def frame_extract(self, path):
        vidObj = cv2.VideoCapture(path)
        success = True
        while success:
            success, image = vidObj.read()
            if success:
                yield image


def predict(model, img):
    fmap, logits = model(img)
    logits = sm(logits)
    _, prediction = torch.max(logits, 1)
    confidence = logits[:, int(prediction.item())].item() * 100
    return int(prediction.item()), confidence


def detectFakeVideo(videoPath):
    im_size = 112
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    train_transforms = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((im_size, im_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ])

    video_dataset = ValidationDataset([videoPath], sequence_length=20, transform=train_transforms)
    model = Model(2)
    model.load_state_dict(torch.load('model/df_model.pt', map_location=torch.device('cpu')))
    model.eval()

    prediction = predict(model, video_dataset[0])
    return prediction


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'GET':
        return render_template('detect.html')

    if request.method == 'POST':
        video = request.files.get('video')
        if not video:
            return jsonify({'error': 'No video file uploaded'}), 400

        filename = secure_filename(video.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video.save(save_path)

        output_label, confidence = detectFakeVideo(save_path)
        os.remove(save_path)

        result = {
            'output': 'REAL' if output_label == 1 else 'FAKE',
            'confidence': confidence
        }

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(result)

        return render_template('detect.html', data=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860)