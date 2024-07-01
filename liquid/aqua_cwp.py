"""
AquaCwp client class.
Handles calling out to authenticate for API requests and forming request payloads
"""

from liquid.aqua_authentication import AquaAuthentication
from liquid.aqua_application_scopes import AquaApplicationScopes
from liquid.aqua_incidents import AquaIncidents


class AquaCwp:
    """Class for calling AquaCwp Specific methods."""

    # pylint: disable=too-few-public-methods

    def __init__(self, client_options=None):
        if client_options is None:
            client_options = {}
        self.client_options = client_options
        self.auth_client = AquaAuthentication(client_options.get("auth_options", {}))
        self.auth_client.authenticate()
        self.application_scopes = AquaApplicationScopes(self.auth_client)
        self.incidents = AquaIncidents(self.auth_client)
