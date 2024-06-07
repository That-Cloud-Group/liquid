import os
from dotenv import load_dotenv

load_dotenv()


class AquaAuthentication:

    def __init__(self, auth_options):
        self.auth_options = auth_options

    def authentication(self):
        if self.auth_options["type"] == "basic":
            self.authenticate_basic()
        elif self.auth_options["type"] == "saas":
            self.authenticate_saas()

    def authenticate_basic(self):
        if os.environ.get("AQUA_USER"):
            pass
