"""
AquaScs client class.
Handles calling out to authenticate for API requests and forming request payloads
"""
from liquid.aqua_authentication import AquaAuthentication
from liquid.aqua_code_scan import AquaCodeScan


class AquaScs:
    """Class for calling AquaScs Specific methods."""

    # pylint: disable=too-few-public-methods

    def __init__(self, client_options=None):
        if client_options is None:
            client_options = {}
        self.client_options = client_options
        self.auth_client = AquaAuthentication(client_options.get("auth_options", {}))
        self.auth_client.authenticate()
        self.code_scan=AquaCodeScan(self.auth_client)