import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


# Test Case 1
def test_home_status(client):
    response = client.get("/")
    assert response.status_code == 200


# Test Case 2
def test_health_status(client):
    response = client.get("/health")
    assert response.status_code == 200


# Test Case 3
def test_invalid_route(client):
    response = client.get("/invalid")
    assert response.status_code == 404


# Test Case 4
def test_post_home(client):
    response = client.post("/")
    assert response.status_code == 405


# Test Case 5
def test_home_message(client):
    response = client.get("/")
    assert b"Backend is running successfully!" in response.data
