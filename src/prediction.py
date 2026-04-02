import numpy as np
import tensorflow as tf
import os
from src.preprocessing import preprocess_image

MODEL_PATH = os.environ.get("MODEL_PATH", "models/plant_disease_model.h5")
CLASS_NAMES = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]

_model = None
_model_mtime = 0


def get_model():
    global _model, _model_mtime
    
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Trained model not found.")

    current_mtime = os.path.getmtime(MODEL_PATH) if os.path.exists(MODEL_PATH) else 0
    
    # Reload if the model isn't loaded yet OR if the file was recently updated by the API container
    if _model is None or current_mtime > _model_mtime:
        _model = tf.keras.models.load_model(MODEL_PATH, compile=False)
        _model_mtime = current_mtime
    return _model


def predict(file_bytes):
    model = get_model()
    arr = preprocess_image(file_bytes)
    probs = model.predict(arr)[0]
    idx = int(np.argmax(probs))
    return {
        "class": CLASS_NAMES[idx],
        "confidence": round(float(np.max(probs)) * 100, 2),
        "all_probabilities": {CLASS_NAMES[i]: round(float(probs[i]) * 100, 2) for i in range(len(CLASS_NAMES))}
    }
