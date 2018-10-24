import numpy as np
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    
    @task
    def predict(self):
        data = {"input": np.random.rand(1, 300).tolist()}
        self.client.post("/predict", json=data)


class WebsiteUser(HttpLocust):
    
    task_set = UserBehavior
