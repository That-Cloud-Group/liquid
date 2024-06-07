""" Aqua client class. 
Handles calling out to authenticate for API requests and forming request payloads
"""


class Aqua:

    def __init__(self, auth_payload):
        self.auth_payload = auth_payload
