from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import os

from src.model import retrain_model

app = FastAPI(title="Potato Disease Retraining API")

DATA_DIR = os.environ.get("DATA_DIR", "data/train")

class RetrainRequest(BaseModel):
    epochs: int = 5

def perform_retraining(epochs: int):
    try:
        print(f"Starting retraining for {epochs} epochs...")
        retrain_model(DATA_DIR, epochs=epochs)
        print("Retraining completed successfully!")
    except Exception as e:
        print(f"Error during retraining: {e}")

@app.post("/api/retrain")
def retrain_endpoint(request: RetrainRequest, background_tasks: BackgroundTasks):
    """
    Triggers model retraining in the background to prevent Streamlit UI freezes 
    and HTTP timeout errors on cloud deployment platforms.
    """
    background_tasks.add_task(perform_retraining, request.epochs)
    return {"status": "success", "message": f"Retraining started in the background for {request.epochs} epochs."}