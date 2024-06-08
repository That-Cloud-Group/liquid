import aqua
class User(aqua):
    def __init__(self, login_id, name, email, password, first_time=False, is_super=False, ui_access=False, actions=[], scopes=[], role="", roles=[], user_type=""):
        self.endpoint = "/api/v1/users"
        self.login_id = login_id
        self.name = name
        self.email = email
        self.password = password
        self.first_time = first_time
        self.is_super = is_super
        # these attributes are only in the v2 of the api
        self.ui_access = ui_access
        self.actions = actions
        self.scopes = scopes
        self.role = role
        self.roles = roles
        self.user_type = user_type
    
    def create(self):
        try:
            data = {
                "id": self.login_id,
                "name": self.name,
                "email": self.email,
                "password": self.password,
                "first_time": self.first_time,
                "admin": self.is_super
            }
        except:
            print("Error Creating User. Please ensure you have set id, name, email and password")
            exit(1)
        
        if aqua.client_type == "saas":
            aqua.SaasCallAqua("POST", f"{aqua.url}{self.endpoint}", data=data)
        return self
    
    def update(self):
        # Can only update name and email
        data = {
            "name": self.name,
            "email": self.email
        }
        if aqua.client_type == "saas":
            aqua.SaasCallAqua("PUT", f"{aqua.url}{self.endpoint}/{self.login_id}", data=data)
        return self
    
    def delete(self):
        if aqua.client_type == "saas":
            self.SaasCallAqua("DELETE", f"{aqua.url}{self.endpoint}/{self.login_id}")
        return self
    