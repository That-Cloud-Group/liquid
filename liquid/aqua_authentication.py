"""Module that handles authentication to Aqua itself."""

import os
import sys
import hashlib
import hmac
import json
import time
from urllib.parse import urlparse
import jwt
import urllib3
import requests


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_REQUEST_HEADERS = {"Content-Type": "application/json; charset=UTF-8"}


class AquaAuthentication:
    """Class that handles authentication functions for aqua"""

    def __init__(self, auth_options=None):
        if auth_options is None:
            auth_options = {}

        self.auth_type = auth_options.get("auth_type", "jwt")
        self.auth_url = auth_options.get("auth_url")
        self.auth_credentials = auth_options.get("auth_credentials")
        self.api_credentials = auth_options.get("api_credentials")
        self.ssl_verify = auth_options.get("ssl_verify", True)
        self.token = None
        self.saas = False

    def authenticate(self):
        """Determines proper authentication method to call"""
        if self.auth_type == "jwt":
            self.authenticate_jwt()
        elif self.auth_type == "saas_api":
            self.authenticate_api_key_saas()

    def authenticate_jwt(self):
        """Authenticates with an aqua server to get a JWT for future requests."""
        print("Authenticating with JWT.")
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
            and not self.saas
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
                print("Authentication Successful")

        elif self.auth_credentials["user"] and self.auth_credentials["password"]:
            # If no AQUA_URL is provided, then this is a SaaS login
            print("No AQUA_URL provided. Assuming this is a SaaS User")
            self.saas = True
            data = {
                "email": self.auth_credentials["user"],
                "password": self.auth_credentials["password"],
            }
            login_response = requests.post(
                "https://api.cloudsploit.com/v2/signin",
                json=data,
                timeout=30,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            if login_response.status_code == 200:
                self.token = login_response.json().get("data").get("token")
                self.auth_url = self.__get_token_endpoint()

        else:
            print("Error: AQUA_USER, AQUA_PASS not set")
            sys.exit(1)

        if login_response.status_code != 200:
            print(login_response.text)
            print("Error: Authentication Failed")
            sys.exit(1)

    def authenticated_get(self, endpoint, params=None):
        """Makes a get request with proper authentication headers"""
        headers = DEFAULT_REQUEST_HEADERS | {"Authorization": f"Bearer {self.token}"}
        get_response = requests.get(
            self.auth_url + "/api" + endpoint,
            params=params,
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

    def authenticate_api_key_saas(self) -> dict:
        """Authenticating to the Aqua API using api key and api secret instead of use-based auth

        Args:
            csp_roles (list, optional): The Aqua role(s) to be associated with the token.
                Defaults to [].
            api_key (str, optional): API_KEY generated upon api key creation. Defaults to "".
            api_secret (str, optional): API_SECRET generated upon api key creation. Defaults to "".
        """
        print("Authenticating with API Key.")
        if not self.api_credentials:
            self.api_credentials = {
                "api_key": os.environ.get("AQUA_API_KEY"),
                "api_secret": os.environ.get("AQUA_API_SECRET"),
                "csp_roles": os.environ.get("AQUA_CSP_ROLES", "").split(", "),
                "api_actions": os.environ.get("AQUA_API_ACTIONS", "").split(", "),
            }

        if (
            self.api_credentials["api_key"]
            and self.api_credentials["api_secret"]
            and self.api_credentials["csp_roles"]
            and self.api_credentials["api_actions"]
        ):
            url = "https://api.cloudsploit.com/v2/tokens"
            body = {
                "validity": 240,
                "allowed_endpoints": self.api_credentials["api_actions"],
                "csp_roles": self.api_credentials["csp_roles"],
            }
            headers = self.__generate_api_header_security(
                self.api_credentials["api_key"],
                self.api_credentials["api_secret"],
                url,
                body,
            )
            login_response = requests.post(
                url,
                verify=self.ssl_verify,
                headers=headers,
                data=body,
                timeout=30,
            )
            if login_response.status_code == 200:
                self.token = login_response.json().get("data")
                self.auth_url = self.__get_token_endpoint()
            else:
                print(login_response.text)
        elif (
            not self.api_credentials["api_key"]
            or not self.api_credentials["api_secret"]
        ):
            print("Error: AQUA_API_KEY or AQUA_API_SECRET not set")
        elif not self.api_credentials["csp_roles"]:
            print("Error: AQUA_CSP_ROLES not set")
        elif not self.api_credentials["api_actions"]:
            print("Error: AQUA_API_ACTIONS not set")

    def __generate_api_header_security(self, api_key, api_secret, url, body):
        body_str = json.dumps(body, separators=(",", ":"))
        timestamp = str(int(time.time() * 1000))
        path = urlparse(url).path
        string = timestamp + "GET" + path + body_str

        secret_bytes = bytes(api_secret, "utf-8")
        string_bytes = bytes(string, "utf-8")

        sig = hmac.new(
            secret_bytes, msg=string_bytes, digestmod=hashlib.sha256
        ).hexdigest()

        headers = {
            "accept": "application/json",
            "x-api-key": api_key,
            "x-signature": sig,
            "x-timestamp": timestamp,
            "content-type": "application/json",
        }

        return headers

    def __get_token_endpoint(self):
        """Looks at JWT Token payload to find custom url for cloud cwp endpoint"""
        proper_cwp = jwt.decode(self.token, options={"verify_signature": False})[
            "csp_metadata"
        ]["urls"]["ese_url"]
        return f"https://{proper_cwp}"
