"""Simple example script to test"""

from dotenv import load_dotenv
import liquid

load_dotenv()

# Saas with user-pass auth
# A lack of "AQUA_URI" set implies we're working with the saas endpoint.
# Implies that environment variables specify:
# AQUA_USER - the user in question
# AQUA_PASS - the password for that user
# AQUA_URL - the endpoint for your aqua instance

AQUA_CLIENT = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": False}})

test_get_firewall_policy = AQUA_CLIENT.auth_client.authenticated_get("cwp",
    "/v2/firewall_policies"
)
test_post_firewall_policy = AQUA_CLIENT.auth_client.authenticated_post("cwp",
    "/v2/firewall_policies", {"name": "test_firewall_policy"}
)
test_get_one_firewall_policy = AQUA_CLIENT.auth_client.authenticated_get("cwp",
    "/v2/firewall_policies/test_firewall_policy"
)
test_put_firewall_policy = AQUA_CLIENT.auth_client.authenticated_put(
    "/v2/firewall_policies/test_firewall_policy",
    {"name": "test_firewall_policy", "description": "test firewall"},
)
test_delete_firewall_policy = AQUA_CLIENT.auth_client.authenticated_delete(
    "/v2/firewall_policies/test_firewall_policy"
)
test_get_incidents = AQUA_CLIENT.incidents.get_incidents(options={})

AQUA_CLIENT.auth_client.authenticated_delete("")
scopes = AQUA_CLIENT.application_scopes.list_application_scopes()

for scope in scopes:
    print(f"Found application scope with name {scope['name']}")
