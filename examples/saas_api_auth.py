"""Simple example script to test"""

from dotenv import load_dotenv
import liquid

load_dotenv()


# Saas with API auth
# A lack of "AQUA_URI" set implies we're working with the saas endpoint.
# Implies that environment variables specify:
# AQUA_API_KEY - API key set in aqua
# AQUA_API_SECRET - API secret set in aqua
# AQUA_CSP_ROLES - Roles associated with that api key
# AQUA_API_ACTIONS - allowed endpoints for the api key
AQUA_CLIENT = liquid.client(
    "aqua_cwp", {"auth_options": {"auth_type": "saas_api", "ssl_verify": True}}
)

scopes = AQUA_CLIENT.application_scopes.list_application_scopes()

for scope in scopes:
    print(f"Found application scope with name {scope['name']}")
