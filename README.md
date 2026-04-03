# Potato Leaf Disease Classifier — MLOps Pipeline

## Project Description
An end-to-end MLOps pipeline that classifies potato leaf diseases (Early Blight, Late Blight, Healthy) using a MobileNetV2 transfer learning model. The system supports live prediction, dataset visualization, bulk data upload, and one-click model retraining through a Streamlit web UI backed by a FastAPI REST API.

---

## Video Demo
[https://youtu.be/MfrZZa2GRTw](https://youtu.be/MfrZZa2GRTw)

## Live URL
[https://mlops-summative-ui.onrender.com](https://mlops-summative-ui.onrender.com)

## Backend API
[https://mlops-summative-lze9.onrender.com/docs](https://mlops-summative-lze9.onrender.com/docs)

---

## Project Structure
```
mlops_summative--1/
├── README.md
├── Dockerfile
├── Dockerfile.backend
├── requirements.txt
├── requirementsUI.txt
├── locustfile.py
├── app.py
├── api.py
├── start.sh
├── notebook/
│   └── notebook.ipynb
├── src/
│   ├── preprocessing.py
│   ├── model.py
│   └── prediction.py
├── data/
│   ├── train/
│   │   ├── Potato___Early_blight/
│   │   ├── Potato___Late_blight/
│   │   └── Potato___healthy/
│   └── test/
└── models/
    └── plant_disease_model.h5
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/DubaKanu/mlops_summative-.git
cd mlops_summative--1
```

### 2. Create Virtual Environment and Install Dependencies
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Train the Model (if .h5 not present)
Open and run `notebook/notebook.ipynb` top to bottom.

### 4. Run Locally (Two Terminals)

Terminal 1 — Backend:
```bash
source venv/bin/activate
uvicorn api:app --host 0.0.0.0 --port 8000
```

Terminal 2 — Frontend:
```bash
source venv/bin/activate
API_URL=https://mlops-summative-ui.onrender.com streamlit run app.py
```

Access at: `http://localhost:8501`

### 5. Run with Docker
```bash
docker build -t potato-disease-app .
docker run -p 8501:8501 potato-disease-app
```

### 6. Run with Multiple Docker Containers (for Locust testing)
```bash
docker run -d -p 8501:8501 --name app1 potato-disease-app
docker run -d -p 8502:8501 --name app2 potato-disease-app
docker run -d -p 8503:8501 --name app3 potato-disease-app
```

---

## Flood Request Simulation (Locust)

To run the Locust flood test, you need two terminals open at the same time.

**Terminal 1 — Start the Backend first:**
```bash
cd mlops_summative--1
source venv/bin/activate
uvicorn api:app --host 0.0.0.0 --port 8000
```
Wait until you see `Uvicorn running on http://0.0.0.0:8000` before proceeding.

**Terminal 2 — Start Locust:**
```bash
cd mlops_summative--1
source venv/bin/activate
locust -f locustfile.py --host=http://localhost:8000
```
Wait until you see `Starting web interface at http://0.0.0.0:8089`.

**Then open your browser and go to:**
```
http://localhost:8089
```
Set the number of users and spawn rate, then click Start. The backend must be running on port 8000 before opening Locust.

### Results Summary
| Containers | Users | Avg Response Time | RPS |
|------------|-------|-------------------|-----|
| 1          | 10    | ~320ms            | ~8  |
| 2          | 50    | ~410ms            | ~18 |
| 3          | 100   | ~530ms            | ~30 |

### Locust Test Screenshots

**Test 1 — 10 Users, 1 Container**

![Locust Test 1](Screenshot%202026-03-25%20at%2012.40.42AM.png)

**Test 2 — 50 Users, 2 Containers**

![Locust Test 2](Screenshot%202026-03-25%20at%2012.54.34AM.png)

**Test 3 — 100 Users, 3 Containers**

![Locust Test 3](Screenshot%202026-03-25%20at%2012.55.46AM.png)

**Test 4 — Response Time Chart**

![Locust Response Time](Screenshot%202026-03-25%20at%2012.59.23AM.png)

**Test 5 — Requests Per Second Chart**

![Locust RPS](Screenshot%202026-03-25%20at%2012.59.39AM.png)

**Test 6 — Final Summary**

![Locust Summary](Screenshot%202026-03-25%20at%201.01.54AM.png)

---

## Features
| Feature | Status |
|---|---|
| Single image prediction | Done |
| Confidence scores per class | Done |
| 3 dataset visualizations with interpretations | Done |
| Bulk image upload and save to dataset | Done |
| One-click model retraining trigger | Done |
| Model uptime / status sidebar | Done |
| FastAPI REST backend | Done |
| Dockerized deployment | Done |
| Locust flood simulation | Done |
| Deployed on Render | Done |
