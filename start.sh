#!/bin/bash

# Create persistent disk directories if they don't exist
mkdir -p /var/data/train/Potato___Early_blight
mkdir -p /var/data/train/Potato___Late_blight
mkdir -p /var/data/train/Potato___healthy
mkdir -p /var/data/models

# Copy initial model to persistent disk if not already there
if [ ! -f /var/data/models/plant_disease_model.h5 ]; then
    if [ -f /app/models/plant_disease_model.h5 ]; then
        cp /app/models/plant_disease_model.h5 /var/data/models/plant_disease_model.h5
        echo "Initial model copied to persistent disk."
    else
        echo "No initial model found. Please retrain from the UI."
    fi
fi

# Start FastAPI background API for model retraining
uvicorn api:app --host 0.0.0.0 --port 8000 &

# Start Streamlit application
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
