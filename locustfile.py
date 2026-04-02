from locust import HttpUser, task, between


class StreamlitUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def load_app(self):
        self.client.get("/", name="Load App")

    @task(1)
    def health_check(self):
        self.client.get("/_stcore/health", name="Health Check")
