import pytest
from unittest.mock import Mock
from liquid.aqua_authentication import AquaAuthentication
from liquid.aqua_application_scopes import AquaApplicationScopes

@pytest.fixture
def mock_auth_client():
    return Mock(spec=AquaAuthentication)

@pytest.fixture
def application_scopes(mock_auth_client):
    return AquaApplicationScopes(auth_client=mock_auth_client)

def test_list_application_scopes(application_scopes, mock_auth_client):
    mock_response = {"result": [{"name": "test_scope"}]}
    mock_auth_client.authenticated_get.return_value = mock_response
    scopes = application_scopes.list_application_scopes()
    assert scopes == [{"name": "test_scope"}]

def test_get_affected_entries(application_scopes, mock_auth_client):
    mock_response = ["test_entity"]
    mock_auth_client.authenticated_get.return_value = mock_response
    affected_entries = application_scopes.get_affected_entries("test_scope")
    assert affected_entries == ["test_entity"]

def test_validate_category_payload(application_scopes):
    valid_payload = {"artifacts": [{"name": "test"}]}
    invalid_payload = {"invalid": "payload"}
    assert application_scopes.validate_category_payload(valid_payload) is True
    assert application_scopes.validate_category_payload(invalid_payload) is False

def test_create_application_scope(application_scopes, mock_auth_client):
    mock_auth_client.authenticated_post.return_value = {"success": True}
    response = application_scopes.create_application_scope(
        name="test_scope", categories={"artifacts": []}, description="test description"
    )
    assert response == {"success": True}

def test_get_application_scope(application_scopes, mock_auth_client):
    mock_response = {"name": "test_scope"}
    mock_auth_client.authenticated_get.return_value = mock_response
    scope = application_scopes.get_application_scope("test_scope")
    assert scope == {"name": "test_scope"}

def test_delete_application_scope(application_scopes, mock_auth_client):
    mock_auth_client.authenticated_delete.return_value = {"success": True}
    response = application_scopes.delete_application_scope("test_scope")
    assert response == {"success": True}

def test_update_application_scope(application_scopes, mock_auth_client):
    mock_auth_client.authenticated_put.return_value = {"success": True}
    response = application_scopes.update_application_scope(
        name="test_scope", categories={"artifacts": []}, description="test description"
    )
    assert response == {"success": True}

def test_list_available_categories(application_scopes, mock_auth_client):
    mock_response = {"categories": [{"name": "test_category"}]}
    mock_auth_client.authenticated_get.return_value = mock_response
    categories = application_scopes.list_available_categories()
    assert categories == {"categories": [{"name": "test_category"}]}

