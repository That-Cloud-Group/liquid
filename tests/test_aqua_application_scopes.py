"""Pytest of the ApplicationScopes api"""

from unittest.mock import Mock
import pytest
from liquid.aqua_authentication import AquaAuthentication
from liquid.aqua_application_scopes import AquaApplicationScopes

# pylint: disable=unused-argument
# pylint: disable=redefined-outer-name
# pylint: disable=missing-module-docstring


@pytest.fixture
def mock_auth_client():
    """Pytest Fixture to mock auth client

    Returns:
        Mock: Mock of the AquaAuthentication class
    """
    return Mock(spec=AquaAuthentication)


@pytest.fixture
def application_scopes(mock_auth_client):
    """Pytest fixture for the AquaApplicationScopes class

    Args:
        mock_auth_client (Mock): Mock of the auth client

    Returns:
        AquaApplicationScopes: AquaApplicationScopes class
    """
    return AquaApplicationScopes(auth_client=mock_auth_client)


def test_list_application_scopes(application_scopes, mock_auth_client):
    """pytest to list application scopes

    Args:
        application_scopes (AquaApplicationScopes): application scopes class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_response = {
        "count": "20",
        "pagesize": "50",
        "result": [{"name": "test_scope"}],
    }
    mock_auth_client.authenticated_get.return_value = mock_response
    scopes = application_scopes.list_application_scopes()
    assert scopes == [{"name": "test_scope"}]

    mock_response_paginate = {
        "count": "100",
        "pagesize": "50",
        "result": [{"name": "double"}],
    }

    mock_auth_client.authenticated_get.return_value = mock_response_paginate
    paginated_scopes = application_scopes.list_application_scopes()
    assert paginated_scopes == [{"name": "double"}, {"name": "double"}]


def test_get_affected_entries(application_scopes, mock_auth_client):
    """Pytest to get affected entries

    Args:
        application_scopes (AquaApplicationScopes): Application scopes class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_response = ["test_entity"]
    mock_auth_client.authenticated_get.return_value = mock_response
    affected_entries = application_scopes.get_affected_entries("test_scope")
    assert affected_entries == ["test_entity"]


def test_validate_category_payload(application_scopes):
    """Pytest Validate category payload

    Args:
        application_scopes (AquaApplicationScopes): Application Scopes Class
    """
    valid_payload = {"artifacts": [{"name": "test"}]}
    invalid_payload = {"invalid": "payload"}
    assert application_scopes.validate_category_payload(valid_payload) is True
    assert application_scopes.validate_category_payload(invalid_payload) is False


def test_create_application_scope(application_scopes, mock_auth_client):
    """Pytest create application scope

    Args:
        application_scopes (AquaApplicationScopes): Application Scopes Class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_auth_client.authenticated_post.return_value = {"success": True}
    response = application_scopes.create_application_scope(
        name="test_scope", categories={"artifacts": []}, description="test description"
    )
    assert response == {"success": True}


def test_get_application_scope(application_scopes, mock_auth_client):
    """Pytest get application scope

    Args:
        application_scopes (AquaApplicationScopes): Application Scopes Class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_response = {"name": "test_scope"}
    mock_auth_client.authenticated_get.return_value = mock_response
    scope = application_scopes.get_application_scope("test_scope")
    assert scope == {"name": "test_scope"}


def test_delete_application_scope(application_scopes, mock_auth_client):
    """PyTest Delete Application Scope

    Args:
        application_scopes (AquaApplicationScopes): Application Scopes Class
        mock_auth_client (Mock): Mock of teh AquaAuthentication
    """
    mock_auth_client.authenticated_delete.return_value = {"success": True}
    response = application_scopes.delete_application_scope("test_scope")
    assert response == {"success": True}


def test_update_application_scope(application_scopes, mock_auth_client):
    """Pytest update application scope

    Args:
        application_scopes (AquaApplicationScopes): Application Scopes Class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_auth_client.authenticated_put.return_value = {"success": True}
    response = application_scopes.update_application_scope(
        name="test_scope", categories={"artifacts": []}, description="test description"
    )
    assert response == {"success": True}


def test_list_available_categories(application_scopes, mock_auth_client):
    """Pytest list available categories

    Args:
        application_scopes (AquaApplicationScopes): Application Scopes Class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_response = {"categories": [{"name": "test_category"}]}
    mock_auth_client.authenticated_get.return_value = mock_response
    categories = application_scopes.list_available_categories()
    assert categories == {"categories": [{"name": "test_category"}]}
