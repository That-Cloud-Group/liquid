"""Simple example script to test"""

import os
import liquid

if not os.getenv("AQUA_URL") and os.getenv("AQUA_USER"):
    # Saas with user-pass auth
    AQUA_CLIENT = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": True}})

elif not os.getenv("AQUA_URL") and os.getenv("AQUA_API_KEY"):
    # Saas with user-pass auth
    AQUA_CLIENT = liquid.client(
        "aqua_cwp", {"auth_options": {"auth_type": "saas_api", "ssl_verify": True}}
    )

elif os.getenv("AQUA_URL") and os.getenv("AQUA_USER"):
    # this is for local aqua installation
    # Example auth with .env set credentials
    AQUA_CLIENT = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": False}})
else:
    AQUA_CLIENT = None

# Example using passed in creds, get these programmatically, people!
# AQUA_CLIENT = liquid.client("aqua_cwp",
# {"auth_options": {"ssl_verify": False,
# "auth_credentials": {"user": "username", "password": "password"}}})

# Low level examples
if AQUA_CLIENT:
    test_get_firewall_policy = AQUA_CLIENT.auth_client.authenticated_get(
        "/v2/firewall_policies"
    )
    test_post_firewall_policy = AQUA_CLIENT.auth_client.authenticated_post(
        "/v2/firewall_policies", {"name": "test_firewall_policy"}
    )
    test_get_one_firewall_policy = AQUA_CLIENT.auth_client.authenticated_get(
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
    print(len(test_get_incidents))
    test_get_incident = AQUA_CLIENT.incidents.get_incident(
        incident_id=test_get_incidents[0]["id"]
    )
    print(test_get_incident)
    test_list_suppression_rules = AQUA_CLIENT.incidents.list_suppression_rules(
        options={}
    )
    print(len(test_list_suppression_rules))

    AQUA_CLIENT.auth_client.authenticated_delete("")
    scopes = AQUA_CLIENT.application_scopes.list_application_scopes()

    for scope in scopes:
        print(f"Found application scope with name {scope['name']}")
