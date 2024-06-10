import requests
from liquid.aqua_authentication import AquaAuthentication
import os

""" Aqua client class.
Handles calling out to authenticate for API requests and forming request payloads
"""


class AquaCwp:

    def __init__(self, client_options={}):
        self.client_options = client_options
        self.auth_client = AquaAuthentication(client_options.get("auth_options", {}))

    def list_application_scopes(self):
        self.auth_client.authenticate()
        raw_scopes_response = self.auth_client.authenticated_get(
            "/v2/access_management/scopes"
        )
        return raw_scopes_response["result"]

    def SaasCallAqua(self, method, path, data=None):
        host = os.getenv("HOST")
        if host:
            token = self.auth.token
            if token:
                if method == "GET":
                    r = requests.get(
                        host + path, headers={"Authorization": "Bearer " + token}
                    )
                    return r
                if method == "DELETE":
                    r = requests.delete(
                        host + path, headers={"Authorization": "Bearer " + token}
                    )
                    return r
                if method == "POST":
                    r = requests.post(
                        host + path,
                        json=data,
                        headers={
                            "Authorization": "Bearer " + token,
                            "Content-Type": "application/json;charset=UTF-8",
                        },
                    )
                    return r
                if method == "PUT":
                    r = requests.put(
                        host + path,
                        json=data,
                        headers={
                            "Authorization": "Bearer " + token,
                            "Content-Type": "application/json;charset=UTF-8",
                        },
                    )
                    return r
            else:
                print("Error calling Aqua")
                return False
        else:
            print("Error: HOST not set")
            return False
