"""Entrypoint into liquid SDK"""

import liquid.aqua_cwp


def client(service, options=None):
    """
    Creates a client class.
    service - a string representing the backend service (e.g. 'aqua_cwp', 'aqua_cspm')
    options - a dictionary with possible keys:
        - 'auth_options' (dict) : authentication options for client, alternatively via
                                    ENV variables with keys:
            - 'auth_type' (string) : authentication type (otherwise default auth used)
            - 'auth_url' (string) : valid host URL
            - 'auth_credentials' (dict) : credentials payload with keys:
                - 'user' (string)
                - 'password' (string)
    """
    if service == "aqua_cwp":
        aqua_cwp_client = liquid.aqua_cwp.AquaCwp(options)
        return aqua_cwp_client
    return None
