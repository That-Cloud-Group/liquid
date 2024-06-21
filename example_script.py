"""Simple example script to test"""

import liquid

# Example auth with .env set credentials
aqua_client = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": False}})

# Example using passed in creds, get these programmatically, people!
# aqua_client = liquid.client("aqua_cwp",
# {"auth_options": {"ssl_verify": False,
# "auth_credentials": {"user": "username", "password": "password"}}})

# Low level examples

test_get_firewall_policy = aqua_client.auth_client.authenticated_get(
    "/v2/firewall_policies"
)
test_post_firewall_policy = aqua_client.auth_client.authenticated_post(
    "/v2/firewall_policies", {"name": "test_firewall_policy"}
)
test_get_one_firewall_policy = aqua_client.auth_client.authenticated_get(
    "/v2/firewall_policies/test_firewall_policy"
)
test_put_firewall_policy = aqua_client.auth_client.authenticated_put(
    "/v2/firewall_policies/test_firewall_policy",
    {"name": "test_firewall_policy", "description": "test firewall"},
)
test_delete_firewall_policy = aqua_client.auth_client.authenticated_delete(
    "/v2/firewall_policies/test_firewall_policy"
)

aqua_client.auth_client.authenticated_delete("")
scopes = aqua_client.application_scopes.list_application_scopes()

for scope in scopes:
    print(f"Found application scope with name {scope['name']}")
