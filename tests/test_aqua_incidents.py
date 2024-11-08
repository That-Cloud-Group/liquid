"""Pytest of the ApplicationScopes api"""

from unittest.mock import Mock
import pytest
from liquid.aqua_authentication import AquaAuthentication
from liquid.aqua_incidents import AquaIncidents

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
def incidents(mock_auth_client):
    """Pytest fixture for the AquaIncidents class

    Args:
        mock_auth_client (Mock): Mock of the auth client

    Returns:
        AquaIncidents: AquaIncidents class
    """
    return AquaIncidents(auth_client=mock_auth_client)


def test_get_incidents(incidents, mock_auth_client):
    """pytest to list incidents

    Args:
        incidents (AquaIncidents): Aqua incidents class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_response = {
        "count": 1,
        "pagesize": "50",
        "result": [{"name": "test_incident"}],
    }
    mock_auth_client.authenticated_get.return_value = mock_response
    incidents_response = incidents.get_incidents({})
    assert incidents_response == [{"name": "test_incident"}]


def test_get_incident_totals(incidents, mock_auth_client):
    """pytest to get incident totals

    Args:
        incidents (AquaIncidents): Aqua incidents class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_response = {
        "count": 1,
        "pagesize": "50",
        "result": [{"name": "test_incident"}],
    }
    mock_auth_client.authenticated_get.return_value = mock_response
    incidents_response = incidents.get_incident_totals({})
    print(incidents_response)
    assert incidents_response["result"] == [{"name": "test_incident"}]


def test_get_incident(incidents, mock_auth_client):
    """pytest to get a single incident

    Args:
        incidents (AquaIncidents):  incidents class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_response = [{"name": "test_incident"}]

    mock_auth_client.authenticated_get.return_value = mock_response
    incidents_response = incidents.get_incident("1")
    assert incidents_response == [{"name": "test_incident"}]


def test_get_incident_timeline(incidents, mock_auth_client):
    """pytest to get an incident timeline

    Args:
        incidents (AquaIncidents):  incidents class
        mock_auth_client (Mock): Mock of the AquaAuthentication
    """
    mock_response = {
        "count": 1,
        "pagesize": "50",
        "result": [{"name": "test_incident"}],
    }
    mock_auth_client.authenticated_get.return_value = mock_response
    incidents_response = incidents.get_incident_timeline("1", {})
    assert incidents_response == [{"name": "test_incident"}]
