"""Simple example script to test"""

import liquid

aqua_client = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": False}})
scopes = aqua_client.list_application_scopes()

for scope in scopes:
    print(f"Found application scope with name {scope['name']}")
