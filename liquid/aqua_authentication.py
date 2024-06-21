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

    def __init__(self, auth_options=None):
        if auth_options is None:
            auth_options = {}

        self.auth_type = auth_options.get("auth_type", "jwt")
        self.auth_url = auth_options.get("auth_url")
        self.auth_credentials = auth_options.get("auth_credentials")
        self.ssl_verify = auth_options.get("ssl_verify", True)
        self.token = None

    def authenticate(self):
        """Determines proper authentication method to call"""
        if self.auth_type == "jwt":
            self.authenticate_jwt()
        elif self.auth_type == "saas":
            self.authenticate_saas()

    def authenticate_jwt(self):
        """Authenticates with an aqua server to get a JWT for future requests."""
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
                self.auth_url + "/api/v1/login",
                verify=self.ssl_verify,
                json=data,
                timeout=5,
            )
            if login_response.status_code == 200:
                self.token = login_response.json().get("token")
            else:
                print(login_response.text)
        else:
            print("Error: AQUA_USER, AQUA_PASS, or AQUA_URL not set")

    def authenticated_get(self, endpoint):
        """Makes a get request with proper authentication headers"""
        headers = DEFAULT_REQUEST_HEADERS | {"Authorization": f"Bearer {self.token}"}
        get_response = requests.get(
            self.auth_url + "/api" + endpoint,
            verify=self.ssl_verify,
            headers=headers,
            timeout=10,
        )
        return get_response.json()

    def authenticated_delete(self, endpoint):
        """Makes a delete request with proper authentication headers"""
        headers = DEFAULT_REQUEST_HEADERS | {"Authorization": f"Bearer {self.token}"}
        delete_response = requests.delete(
            self.auth_url + "/api" + endpoint,
            verify=self.ssl_verify,
            headers=headers,
            timeout=10,
        )
        return delete_response

    def authenticated_post(self, endpoint, data):
        """Makes a post request with proper authentication headers"""
        headers = DEFAULT_REQUEST_HEADERS | {"Authorization": f"Bearer {self.token}"}
        post_response = requests.post(
            self.auth_url + "/api" + endpoint,
            verify=self.ssl_verify,
            headers=headers,
            json=data,
            timeout=10,
        )
        return post_response

    def authenticated_put(self, endpoint, data):
        """Makes a put request with proper authentication headers"""
        headers = DEFAULT_REQUEST_HEADERS | {"Authorization": f"Bearer {self.token}"}
        put_response = requests.put(
            self.auth_url + "/api" + endpoint,
            verify=self.ssl_verify,
            headers=headers,
            json=data,
            timeout=10,
        )
        return put_response

    def authenticate_saas(self):
        """Authenticates with SaaS endpoint using API tokens"""
        print("Authenticating with SaaS.")
