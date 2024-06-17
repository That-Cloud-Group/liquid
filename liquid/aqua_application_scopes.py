"""Module to handle all operations with application scopes"""

APPLICATION_SCOPE_URI = "/v2/access_management/scopes"


class AquaApplicationScopes:
    """Class to create methods for interacting with all application scope operations"""

    def __init__(self, auth_client):
        self.auth_client = auth_client

    def list_application_scopes(self):
        """Lists application scopes in aqua, returning an array of scope data."""
        self.auth_client.authenticate()
        raw_scopes_response = self.auth_client.authenticated_get(APPLICATION_SCOPE_URI)
        return raw_scopes_response["result"]

    def get_affected_entries(self, application_scope_name=None):
        """Get all entities affected by a specific application scope,
        such as Aqua Policies and Services"""
        self.auth_client.authenticate()
        affected_entries = self.auth_client.authenticated_get(
            f"{APPLICATION_SCOPE_URI}/{application_scope_name}/affected_entries"
        )
        return affected_entries

    def validate_category_payload(self, categories):
        """Determines if payload for categories is correctly formatted for API"""
        if categories:
            if "artifacts" in categories.keys():
                return True
        return False

    def create_application_scope(self, name=None, categories=None, description=None):
        """Creates a new application scope with name and category payload."""
        self.validate_category_payload(categories)

        created_application_scope = self.auth_client.authenticated_post(
            APPLICATION_SCOPE_URI,
            {"name": name, "categories": categories, "description": description},
        )

        return created_application_scope.json()
