"""Simple example script to test"""

import liquid
import os
if os.getenv("AQUA_SAAS"):
    aqua_client = liquid.client("aqua_cwp", {"auth_options": {
        "auth_type": "saas",
        "ssl_verify": True}})
    scopes = aqua_client.list_application_scopes()

    for scope in scopes:
        print(f"Found application scope with name {scope['name']}")

if os.getenv("AQUA_JWT"):
    aqua_client = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": False}})
    scopes = aqua_client.list_application_scopes()

    for scope in scopes:
        print(f"Found application scope with name {scope['name']}")

