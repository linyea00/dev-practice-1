"""
app.py test
"""

import pytest

from app import app


@pytest.fixture
def client():
    # Configure the Flask test client
    with app.test_client() as client:
        yield client


def test_home(client):
    # Send a GET request to the "/" endpoint
    response = client.get("/")
    # Check that the HTTP status code is 200 (OK)
    assert response.status_code == 200
    # Check that the returned content is the expected string
    assert response.data.decode('utf-8') == "Hello, CI/CD with Docker!"
