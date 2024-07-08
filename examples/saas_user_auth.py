"""Simple example script to test"""

from dotenv import load_dotenv
import liquid

load_dotenv()

# Saas with user-pass auth
# A lack of "AQUA_URI" set implies we're working with the saas endpoint.
# Implies that environment variables specify:
# AQUA_USER - the user in question
# AQUA_PASS - the password for that user
AQUA_CLIENT = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": True}})

test_get_incidents = AQUA_CLIENT.incidents.get_incidents(options={})
if test_get_incidents:
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
