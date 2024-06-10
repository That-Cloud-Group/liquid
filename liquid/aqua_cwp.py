"""
AquaCwp client class.
Handles calling out to authenticate for API requests and forming request payloads
"""

from liquid.aqua_authentication import AquaAuthentication


class AquaCwp:
    """Class for calling AquaCwp Specific methods."""

    def __init__(self, client_options=None):
        if client_options is None:
            client_options = {}
        self.client_options = client_options
        self.auth_client = AquaAuthentication(client_options.get("auth_options", {}))

    def list_application_scopes(self):
        """Lists application scopes in aqua, returning an array of scope data."""
        self.auth_client.authenticate()
        raw_scopes_response = self.auth_client.authenticated_get(
            "/v2/access_management/scopes"
        )
        return raw_scopes_response["result"]

    def get_affected_entries(self, application_scope_name=None):
        """Get all entities affected by a specific application scope,
        such as Aqua Policies and Services"""
        self.auth_client.authenticate()
        affected_entries = self.auth_client.authenticated_get(
            f"/v2/access_management/scopes/{application_scope_name}/affected_entries"
        )
        return affected_entries
