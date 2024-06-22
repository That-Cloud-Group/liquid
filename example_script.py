"""Simple example script to test"""

import liquid
import os
if not os.getenv("AQUA_URL") and os.getenv("AQUA_USER"):
    #Saas with user-pass auth
    aqua_client = liquid.client("aqua_cwp", {"auth_options": {
        "ssl_verify": True}})
    scopes = aqua_client.application_scopes.list_application_scopes()

    for scope in scopes:
        print(f"Found application scope with name {scope['name']}")

elif not os.getenv("AQUA_URL") and os.getenv("AQUA_API_KEY"):
    #Saas with user-pass auth
    aqua_client = liquid.client("aqua_cwp", {"auth_options": {
        "ssl_verify": True}})
    scopes = aqua_client.application_scopes.list_application_scopes()

    for scope in scopes:
        print(f"Found application scope with name {scope['name']}")

elif os.getenv("AQUA_URL") and os.getenv("AQUA_USER"):
    # this is for local aqua installation
    aqua_client = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": False}})
    scopes = aqua_client.application_scopes.list_application_scopes()

    for scope in scopes:
        print(f"Found application scope with name {scope['name']}")

