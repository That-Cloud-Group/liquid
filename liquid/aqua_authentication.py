"""Module that handles authentication to Aqua itself."""

import os
from dotenv import load_dotenv
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
DEFAULT_REQUEST_HEADERS = {"Content-Type": "application/json; charset=UTF-8"}


class AquaAuthentication:
    """Class that handles authentication functions for aqua"""

    def __init__(self, auth_options={}):
        self.auth_type = auth_options.get("auth_type", "jwt")
        self.auth_url = auth_options.get("auth_url")
        self.auth_credentials = auth_options.get("auth_credentials")
        self.ssl_verify = auth_options.get("ssl_verify", True)
        self.token = None

    def authenticate(self):
        if self.auth_type == "jwt":
            self.authenticate_jwt()
        elif self.auth_type == "saas":
            self.authenticate_saas()

    def authenticate_jwt(self):
        if not self.auth_credentials:
            self.auth_credentials = {
                "user": os.environ.get("AQUA_USER"),
                "password": os.environ.get("AQUA_PASS"),
            }

        if not self.auth_url:
            self.auth_url = os.environ.get("AQUA_URL")

        if (
            self.auth_credentials["user"]
            and self.auth_credentials["password"]
            and self.auth_url
        ):
            data = {
                "id": self.auth_credentials["user"],
                "password": self.auth_credentials["password"],
            }
            login_response = requests.post(
                self.auth_url + "/api/v1/login", verify=self.ssl_verify, json=data
            )
            if login_response.status_code == 200:
                self.token = login_response.json().get("token")
            else:
                print(login_response.text)
                return False
        else:
            print("Error: AQUA_USER, AQUA_PASS, or AQUA_URL not set")
            return False

    def authenticated_get(self, endpoint):
        headers = DEFAULT_REQUEST_HEADERS | {"Authorization": f"Bearer {self.token}"}
        get_response = requests.get(
            self.auth_url + "/api" + endpoint, verify=False, headers=headers
        )
        return get_response.json()
