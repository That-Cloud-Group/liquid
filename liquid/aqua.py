import requests
import aqua_authentication
import os
import Services

""" Aqua client class.
Handles calling out to authenticate for API requests and forming request payloads
"""


class Aqua:

    def __init__(self, auth_payload):
        self.auth = aqua_authentication().authentication(auth_payload)
        self.client_type = auth_payload["client_type"]
        self.url = auth_payload["AQUA_URL"]
        self.user = auth_payload["AQUA_USER"]
        self.password = auth_payload["AQUA_PASS"]
        self.sslVerify = auth_payload["AQUA_SSL_VERIFY"]

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
