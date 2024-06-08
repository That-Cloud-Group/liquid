import aqua
class Label(aqua):
    def __init__(self, name, description="", author="", created=""):
        self.endpoint = "/api/v1/settings/labels"
        self.name = name
        self.description = description
        self.author = author
        self.created = created

    def create(self):
        try:
            data = {
                "name": self.name,
                "description": self.description
            }
        except:
            print("Error Creating Label. Please ensure you have set name")
            exit(1)
        
        if aqua.client_type == "saas":
            aqua.SaasCallAqua("POST", f"{aqua.url}{self.endpoint}", data=data)
        return self
    
    def update(self):
        # Can only update name and email
        data = {
            "description": self.description
        }
        if aqua.client_type == "saas":
            aqua.SaasCallAqua("PUT", f"{aqua.url}{self.endpoint}/{self.name}", data=data)
        return self
    
    def delete(self):
        if aqua.client_type == "saas":
            self.SaasCallAqua("DELETE", f"{aqua.url}{self.endpoint}/{self.name}")
        return self
    
    def attach(self, resource_id, resource_type):
        data = {
            "id": resource_id,
            "type": resource_type
        }
        if aqua.client_type == "saas":
            self.SaasCallAqua("POST", f"{aqua.url}{self.endpoint}/{self.name}/attach")
        return self
    
    def detach(self, resource_id, resource_type):
        data = {
            "id": resource_id,
            "type": resource_type
        }
        if aqua.client_type == "saas":
            self.SaasCallAqua("POST", f"{aqua.url}{self.endpoint}/{self.name}/unattach")
        return self
    