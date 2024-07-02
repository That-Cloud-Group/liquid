"""Module to handle all operations with application scopes"""

ACCESS_MANAGEMENT_URI = "/v2/access_management"
APPLICATION_SCOPE_URI = f"{ACCESS_MANAGEMENT_URI}/scopes"


class AquaApplicationScopes:
    """Class to create methods for interacting with all application scope operations"""

    def __init__(self, auth_client):
        self.auth_client = auth_client

    def list_application_scopes(self):
        """Lists application scopes in aqua, returning an array of scope data."""
        scopes = self.auth_client.authenticated_get(APPLICATION_SCOPE_URI)
        if int(scopes["count"]) > int(scopes["pagesize"]):
            number_of_pages = int(scopes["count"]) // int(scopes["pagesize"])
            for page in range(number_of_pages - 1):
                more_scopes = self.auth_client.authenticated_get(
                    f"{APPLICATION_SCOPE_URI}",
                    params={"page": str(page + 2)},
                )
                scopes["result"] += more_scopes["result"]

        return scopes["result"]

    def get_affected_entries(self, application_scope_name=None):
        """Get all entities affected by a specific application scope,
        such as Aqua Policies and Services"""
        affected_entries = self.auth_client.authenticated_get(
            f"{APPLICATION_SCOPE_URI}/{application_scope_name}/affected_entities"
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

        return created_application_scope

    def get_application_scope(self, application_scope_name):
        """Pulls information about given application scope."""
        application_scope_response = self.auth_client.authenticated_get(
            f"{APPLICATION_SCOPE_URI}/{application_scope_name}"
        )
        return application_scope_response

    def delete_application_scope(self, application_scope_name):
        """Deletes application scope by name"""
        application_scope_delete_response = self.auth_client.authenticated_delete(
            f"{APPLICATION_SCOPE_URI}/{application_scope_name}"
        )
        return application_scope_delete_response

    def update_application_scope(self, name=None, categories=None, description=None):
        """Updates an existing application scope with name and category payload."""
        self.validate_category_payload(categories)

        update_application_scope = self.auth_client.authenticated_put(
            f"{APPLICATION_SCOPE_URI}/{name}",
            {"name": name, "categories": categories, "description": description},
        )

        return update_application_scope

    def list_available_categories(self):
        """List all RBAC (Role-Based Access Control) categories"""
        available_categories = self.auth_client.authenticated_get(
            f"{ACCESS_MANAGEMENT_URI}/categories"
        )
        return available_categories
