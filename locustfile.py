from locust import HttpUser, task, between


class PlantDiseaseUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def health_check(self):
        self.client.get("/api/status", name="Model Status")

    @task(1)
    def root(self):
        self.client.get("/docs", name="API Docs")
