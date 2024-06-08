import os
from dotenv import load_dotenv
import requests

load_dotenv()


class AquaAuthentication:

    def __init__(self, auth_options):
        self.auth_options = auth_options

    def authentication(self):
        if self.auth_options["type"] == "basic":
            self.authenticate_basic()
            return self
        elif self.auth_options["type"] == "saas":
            self.authenticate_saas()
            return self

    def authenticate_basic(self):
        if os.environ.get("AQUA_USER"):
            pass

    def authenticate_saas(self):
        user = os.environ.get("AQUA_USER")
        password = os.environ.get("AQUA_PASS")
        url = os.environ.get("AQUA_URL")
        if user and password and url:
            data = {
                "id": user,
                "password": password
            }
            r = requests.post(url + '/api/v1/login', json=data)
            if r.status_code == 200:
                self.token = r.json().get('token')
            else:
                print(r.text)
                return False
        else:
            print("Error: AQUA_USER, AQUA_PASS, or AQUA_URL not set")
            return False