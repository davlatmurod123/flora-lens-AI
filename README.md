# 🌼 FloraLens — Flower Detective Extraordinaire

<div align="center">
  <img src="https://images.unsplash.com/photo-1468327768560-75b778cbb551?auto=format&fit=crop&w=1200&q=80" alt="Flower field" width="100%" />
</div>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-2.x-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img alt="Model" src="https://img.shields.io/badge/Model-102%20Flower%20Species-8A2BE2?style=for-the-badge" />
</p>

> “A flower is just a plant with excellent branding.” — some very wise botanist, probably

## ⭐ Why this project is ridiculously cool

FloraLens is a flower recognition app that lets you upload a photo and instantly get the top predicted flower species. It combines a trained deep learning model with a simple browser UI and a lightning-fast API backend.

It is the kind of project that makes you feel like a wizard:

- Upload a flower pic
- API analyzes it
- Model makes a guess
- UI shows the top 3 candidates with confidence bars

It is basically a tiny AI botanist. No lab coat required.

---

## ✨ Features

- 🌸 Image upload from browser or drag-and-drop
- 🧠 Deep learning classification using EfficientNet-B0
- 📊 Top-3 predictions with confidence scores
- ⚡ FastAPI backend for quick responses
- 🌐 Simple web interface served directly from the app
- 🏷️ Trained on Oxford Flowers 102 dataset categories

---

## 🖼️ Screenshots

<div align="center">
  <img src="https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?auto=format&fit=crop&w=900&q=80" alt="Flower close-up" width="32%" />
  <img src="https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?auto=format&fit=crop&w=900&q=80" alt="Pink flowers" width="32%" />
  <img src="https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=900&q=80" alt="Garden flowers" width="32%" />
</div>

<div align="center">
  <img src="https://images.unsplash.com/photo-1470509037663-253afd7f0f51?auto=format&fit=crop&w=1200&q=80" alt="Flower identification UI concept" width="100%" />
</div>

---

## 🚀 How it works

```mermaid
flowchart LR
    A[User uploads flower photo] --> B[Browser UI]
    B --> C[FastAPI /predict endpoint]
    C --> D[Image preprocessing]
    D --> E[EfficientNet-B0 model]
    E --> F[Top 3 flower predictions]
    F --> G[Confidence bars in browser]
```

The app:

1. Accepts an image file from the browser
2. Converts and normalizes the image for model input
3. Runs inference with a pretrained EfficientNet model
4. Returns the best matching species and confidence values
5. Displays the result with a clean visual interface

---

## 🧪 Tech stack

- Python
- FastAPI
- PyTorch
- TorchVision
- timm
- Pillow
- HTML + CSS + JavaScript

---

## 📦 Project structure

```text
flora-lens/
├── main.py                # FastAPI backend and prediction logic
├── index.html             # Browser UI
├── requirements.txt       # Python dependencies
├── models/
│   ├── best_model.pt      # trained model weights
│   ├── classes.json       # flower class names
│   └── history.json       # training history / metadata
├── README.md              # project documentation
└── .gitignore             # optional local project ignore rules
```

---

## ⚙️ Installation

1. Clone the project

```bash
git clone https://github.com/your-username/flora-lens.git
cd flora-lens
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate it

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the app

Start the backend server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Then open:

```text
http://127.0.0.1:8000/
```

The browser UI will load and let you upload a flower photo.

---

## 🧠 API endpoint

### POST /predict

Upload an image and receive top predictions.

#### Example

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -F "file=@flower.jpg"
```

#### Response

```json
{
  "predictions": [
    {"species": "daisy", "confidence": 0.9234},
    {"species": "sunflower", "confidence": 0.0521},
    {"species": "rose", "confidence": 0.0188}
  ]
}
```

---

## 🌼 Model notes

This project uses a model trained to recognize flower classes from the Oxford Flowers 102 dataset. In practical terms:

- it works best on flowers that look like the training set
- it may be confused by weird lighting, blurry shots, or non-flower objects
- near 100% confidence is rare in the real world, and that is totally normal

So yes, the AI is smart — but not magically smarter than a botanist with a camera.

---

## 🏆 Fun use cases

- Identify flowers during a walk in the park
- Explore botanical species from photos
- Build a tiny AI flower assistant for learning
- Turn this into a garden companion app later

---

## 🔮 Future upgrades

- Add species descriptions and care tips
- Support multiple languages
- Improve model accuracy with data augmentation
- Add a history of predictions
- Build a mobile app version
- Add a real “guess confidence + explanation” panel

---

## ✅ Current status

This project is a working local demo with:

- a trained model
- browser upload interface
- prediction API
- flower classification flow

It is ready for experimentation, learning, and extension.

---

## 💬 Final thought

If flowers had a social media profile, FloraLens would be the app that helps them say:

> “Hi, I’m a rose, but I am not actually a rose.”

You upload the bloom, the model tries its best, and the magic of computer vision does the rest.

---

<p align="center">
  <img src="https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=1200&q=80" alt="Beautiful flowers" width="100%" />
</p>

<p align="center">
  <strong>⭐ Made with curiosity, flowers, and a little bit of AI chaos ⭐</strong>
</p>
