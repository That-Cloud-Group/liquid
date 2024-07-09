"""Module to handle all operations with aqua users"""

USER_URI = "/v2/users"


class AquaUsers:
    """Class to create methods for interacting with user operations"""

    def __init__(self, auth_client):
        self.auth_client = auth_client

    def list_application_scopes(self):
        """Lists users in aqua, returning an array of"""
        users = self.auth_client.authenticated_get(USER_URI)
        if int(users["count"]) > int(users["pagesize"]):
            number_of_pages = int(users["count"]) // int(users["pagesize"])
            for page in range(number_of_pages - 1):
                more_users = self.auth_client.authenticated_get(
                    f"{USER_URI}",
                    params={"page": str(page + 2)},
                )
                users["result"] += more_users["result"]

        return users["result"]

    def change_users_own_password(self, current_password, new_password):
        """Updates a users own password.

        :param current_password: String of current password
        :param new_password: String of new password to set

        returns: Raw post response.

        """
        change_password = self.auth_client.authenticated_post(
            "/v2/self_service/change_password",
            {"current_password": current_password, "new_password": new_password},
        )

        return change_password

    def reset_user_passwords(self, login_ids):
        """Resets passwords for given ids

        :params login_ids: Array of login ids to reset

        returns: Raw post response.

        """

        reset_passwords = self.auth_client.authenticated_post(
            "/v2/users/reset_password", {"login_ids": login_ids}
        )

        return reset_passwords
