from locust import HttpUser, task, between
import os
import random

# Find a sample image to use for testing.
# This assumes the script is run from the project root.
SAMPLE_IMAGE_DIR = "data/train/Potato___healthy"
try:
    SAMPLE_IMAGES = [os.path.join(SAMPLE_IMAGE_DIR, f) for f in os.listdir(SAMPLE_IMAGE_DIR)]
except FileNotFoundError:
    SAMPLE_IMAGES = []


class PlantDiseaseUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def health_check(self):
        self.client.get("/api/status", name="/api/status")

    @task(4)
    def predict(self):
        if not SAMPLE_IMAGES:
            return
        image_path = random.choice(SAMPLE_IMAGES)
        with open(image_path, "rb") as image_file:
            files = {"file": (os.path.basename(image_path), image_file.read(), "image/jpeg")}
            self.client.post("/api/predict", files=files, name="/api/predict")
