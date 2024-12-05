from locust import FastHttpUser , task, between

class UserBehavior(FastHttpUser ):
    wait_time = between(0.1, 0.5)  

    @task
    def send_notification(self):
        response = self.client.post("/send-notification/", json={
           "client_id": "client123",
           "recipient": "sbdfh@hdsf",
           "channel": "email",
           "message": "Your package has been shipped.",
           "package_status": "shipped"
        })
        print(f"Response status: {response.status_code}, Response body: {response.text}")

    