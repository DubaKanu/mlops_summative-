from fastapi import FastAPI, BackgroundTasks, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import time

from src.model import retrain_model
from src.prediction import predict, MODEL_PATH

app = FastAPI(title="Potato Disease API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = os.environ.get("DATA_DIR", "data/train")
CLASS_NAMES = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]


class RetrainRequest(BaseModel):
    epochs: int = 5


def perform_retraining(epochs: int):
    try:
        print(f"Starting retraining for {epochs} epochs...")
        retrain_model(DATA_DIR, epochs=epochs)
        print("Retraining completed successfully!")
    except Exception as e:
        print(f"Error during retraining: {e}")


@app.get("/api/status")
def status():
    if os.path.exists(MODEL_PATH):
        mtime = os.path.getmtime(MODEL_PATH)
        last_trained = time.strftime("%Y-%m-%d %H:%M", time.localtime(mtime))
        size_mb = round(os.path.getsize(MODEL_PATH) / (1024 * 1024), 2)
        return {"status": "online", "last_trained": last_trained,
                "model_size": f"{size_mb} MB", "classes": len(CLASS_NAMES)}
    return {"status": "offline"}


@app.post("/api/predict")
async def predict_endpoint(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = predict(contents)
        return result
    except FileNotFoundError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/retrain")
def retrain_endpoint(request: RetrainRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(perform_retraining, request.epochs)
    return {"status": "success", "message": f"Retraining started in the background for {request.epochs} epochs."}
