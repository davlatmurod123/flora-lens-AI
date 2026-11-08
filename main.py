import io
import json
from pathlib import Path

import timm
import torch
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from PIL import Image
from torchvision import transforms

BASE_DIR = Path(__file__).parent
MAX_FILE_MB = 10

# 1. Load flower names and the trained model once, at server startup
with open(BASE_DIR / "models" / "classes.json", encoding="utf-8") as f:
    CLASSES = json.load(f)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = timm.create_model("efficientnet_b0", pretrained=False, num_classes=len(CLASSES))
model.load_state_dict(torch.load(BASE_DIR / "models" / "best_model.pt", map_location=device))
model.to(device).eval()

# 2. Same preprocessing as validation/test in training
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

app = FastAPI(title="FloraLens API")  # <- app name (1 of 3)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "species": len(CLASSES), "device": device}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file.")

    data = await file.read()
    if len(data) > MAX_FILE_MB * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"Image is too large (max {MAX_FILE_MB} MB).")

    try:
        img = Image.open(io.BytesIO(data)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Could not read the image.")

    x = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        probs = torch.softmax(model(x), dim=1)[0]
    top = probs.topk(3)

    return {
        "predictions": [
            {"species": CLASSES[i], "confidence": round(p, 4)}
            for p, i in zip(top.values.tolist(), top.indices.tolist())
        ]
    }