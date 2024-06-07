class User:
    def __init__(self, login_id, name, email, password, first_time, is_super, ui_access, actions, scopes, role, roles, type):
        self.login_id = login_id
        self.name = name
        self.email = email
        self.password = password
        self.first_time = first_time
        self.is_super = is_super
        self.ui_access = ui_access
        self.actions = actions
        self.scopes = scopes
        self.role = role
        self.roles = roles
        self.type = type
