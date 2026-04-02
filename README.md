# 🥔 Potato Leaf Disease Classifier — MLOps Pipeline

## Project Description
An end-to-end MLOps pipeline that classifies potato leaf diseases (Early Blight, Late Blight, Healthy) using a MobileNetV2 transfer learning model. The system supports live prediction, dataset visualization, bulk data upload, and one-click model retraining — all through a Streamlit web UI.

---

## 🎥 Video Demo
[YouTube Demo Link — add your link here]

## 🌐 Live URL
[https://mlops-summative-ui.onrender.com](https://mlops-summative-ui.onrender.com)

---

## 📁 Project Structure
```
mlops_summative--1/
├── README.md
├── Dockerfile
├── requirements.txt
├── locustfile.py
├── app.py
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

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd mlops_summative--1
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model (if .h5 not present)
Open and run `notebook/notebook.ipynb` top to bottom.

### 4. Run the App Locally
```bash
streamlit run app.py
```

### 5. Run with Docker
```bash
docker build -t potato-disease-app .
docker run -p 8501:8501 potato-disease-app
```
Access at: `http://localhost:8501`

### 6. Run with Multiple Docker Containers (for Locust testing)
```bash
docker run -d -p 8501:8501 --name app1 potato-disease-app
docker run -d -p 8502:8501 --name app2 potato-disease-app
docker run -d -p 8503:8501 --name app3 potato-disease-app
```

---

## 🌊 Flood Request Simulation (Locust)

### Run Locust
```bash
locust -f locustfile.py --host=http://localhost:8501
```
Open `http://localhost:8089` in your browser, set the number of users and spawn rate, then start the test.

### Results
| Containers | Users | Avg Response Time | RPS |
|------------|-------|-------------------|-----|
| 1          | 10    | ~320ms            | ~8  |
| 2          | 50    | ~410ms            | ~18 |
| 3          | 100   | ~530ms            | ~30 |

> Replace the table above with your actual recorded results.

---

## ✅ Features
| Feature | Status |
|---|---|
| Single image prediction | ✅ |
| Confidence scores per class | ✅ |
| 3 dataset visualizations with interpretations | ✅ |
| Bulk image upload + save to dataset | ✅ |
| One-click model retraining trigger | ✅ |
| Training curves after retraining | ✅ |
| Model uptime / status sidebar | ✅ |
| Dockerized deployment | ✅ |
| Locust flood simulation | ✅ |


![
[alt text](<Screenshot 2026-03-25 at 12.55.46 AM.png>)
](<Screenshot 2026-03-25 at 1.01.54 AM.png>)
![alt text](<Screenshot 2026-03-25 at 12.59.39 AM.png>)
![alt text](<Screenshot 2026-03-25 at 12.54.34 AM.png>)
![alt text](<Screenshot 2026-03-25 at 12.40.42 AM.png>)
![alt text](<Screenshot 2026-03-25 at 12.59.23 AM.png>)