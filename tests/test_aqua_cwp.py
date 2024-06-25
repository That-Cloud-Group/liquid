import pytest
from unittest.mock import Mock
from liquid.aqua_cwp import AquaCwp
from liquid.aqua_authentication import AquaAuthentication

@pytest.fixture
def mock_auth_client():
    return Mock(AquaAuthentication({"auth_credentials": {"user": "test_user", "password": "test_pass"}}))

@pytest.fixture
def cwp_client(mock_auth_client):
    return AquaCwp(client_options={"auth_options": {"auth_credentials": {"user": "test_user", "password": "test_pass"}}})

def test_init(cwp_client, mock_auth_client):
    # need to add assertions
    pass

# Add more tests for other methods in AquaCwp

