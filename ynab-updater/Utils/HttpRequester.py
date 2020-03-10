import requests


class HttpRequester:
    def __init__(self, auth_token):
        self.authorization_token = auth_token
        pass

    def make_request(self, endpoint):
        response = requests.get(endpoint, headers={"Authorization": self.authorization_token}).json()
        return response