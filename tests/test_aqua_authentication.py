import pytest
import os
from unittest.mock import patch, Mock
from liquid.aqua_authentication import AquaAuthentication

FAKE_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJjc3BfbWV0YWRhdGEiOnsidXJscyI6eyJlc2VfdXJsIjoiaHR0cHM6Ly93d3cuZXhhbXBsZS5jb20ifX19.CEIqHnkxR-4DxACQSbuNXArl3qPZ07twZnY6Wi94Rgs"

@pytest.fixture
def auth_client():
    return AquaAuthentication(auth_options={"auth_credentials": {"user": "test_user", "password": "test_pass"}})

def test__generate_api_header_security(auth_client):
    api_key = "test_api_key"
    api_secret = "test_api_secret"
    url = "https://example.com/api"
    body = {"example": "payload"}
    headers = auth_client._AquaAuthentication__generate_api_header_security(api_key, api_secret, url, body)
    assert "x-api-key" in headers
    assert "x-signature" in headers
    assert "x-timestamp" in headers

def test_authenticate_jwt(auth_client, monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": {"token": FAKE_TOKEN}}
    monkeypatch.setenv("AQUA_USER", "test_user")
    monkeypatch.setenv("AQUA_PASS", "test_pass")
    monkeypatch.setenv("AQUA_URL", "https://example.com")
    monkeypatch.setattr("requests.post", lambda *args, **kwargs: mock_response)

    auth_client.authenticate_jwt()
    assert auth_client.token == FAKE_TOKEN

def test_authenticate_api_key_saas(auth_client, monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": FAKE_TOKEN}
    monkeypatch.setenv("AQUA_API_KEY", "test_api_key")
    monkeypatch.setenv("AQUA_API_SECRET", "test_api_secret")
    monkeypatch.setenv("AQUA_CSP_ROLES", "test_role")
    monkeypatch.setenv("AQUA_API_ACTIONS", "test_action")
    monkeypatch.setattr("requests.post", lambda *args, **kwargs: mock_response)

    auth_client.authenticate_api_key_saas()
    assert auth_client.token == FAKE_TOKEN

def test_authenticated_get(auth_client, monkeypatch):
    mock_response = Mock()
    mock_response.json.return_value = {"test": "data"}
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response)
    auth_client.token = FAKE_TOKEN
    auth_client.auth_url = "https://example.com"

    response = auth_client.authenticated_get("/test")
    assert response == {"test": "data"}

# Add more tests for authenticated_post, authenticated_put, authenticated_delete, and other methods
