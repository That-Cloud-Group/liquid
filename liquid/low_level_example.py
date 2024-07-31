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
AQUA_SCS_CLIENT = liquid.client("aqua_scs", {"auth_options": {"ssl_verify": True}})

# Call the user management endpoint manually.
user_info = AQUA_CLIENT.auth_client.authenticated_get("cwp","/v2/users")
print(user_info)

#get code scan results
print(AQUA_SCS_CLIENT.code_scans.get_results_summary())