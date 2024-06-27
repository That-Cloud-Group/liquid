"""Pytest of the Aqua CWP Client"""

from unittest.mock import Mock
import pytest
from liquid.aqua_cwp import AquaCwp
from liquid.aqua_authentication import AquaAuthentication

# pylint: disable=unused-argument
# pylint: disable=redefined-outer-name
# pylint: disable=missing-module-docstring


@pytest.fixture
def mock_auth_client():
    """Pytest mock client for AquaAuthentication

    Returns:
        Mock: Mock object for AquaAuthentication
    """

    return Mock(
        AquaAuthentication(
            {"auth_credentials": {"user": "test_user", "password": "test_pass"}}
        )
    )


@pytest.fixture
def cwp_client(mock_auth_client):
    """Pytest fixture for AquaCwp client

    Args:
        mock_auth_client (Mock): Mock of auth client

    Returns:
        AquaCwp: AquaCwp client
    """
    return AquaCwp(
        client_options={
            "auth_options": {
                "auth_credentials": {"user": "test_user", "password": "test_pass"}
            }
        }
    )


def test_init(cwp_client, mock_auth_client):
    """Pytest init script

    Args:
        cwp_client (AquaCwp): AquaCwp Class
        mock_auth_client (Mock): Mock of the auth client
    """
    # need to add assertions
    # pylint: disable=unnecessary-pass
    pass


# Add more tests for other methods in AquaCwp
