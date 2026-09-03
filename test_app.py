import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200


def test_home_message(client):
    response = client.get('/')
    data = response.get_json()
    assert "message" in data


def test_health_status(client):
    response = client.get('/health')
    data = response.get_json()
    assert data["status"] == "ok"


def test_home_returns_json(client):
    response = client.get('/')
    assert response.content_type == "application/json"


def test_invalid_route(client):
    response = client.get('/invalid')
    assert response.status_code == 404


def test_invalid_route_returns_json(client):
    # Confirms the custom 404 handler is actually wired up,
    # not just Flask's default HTML 404 page.
    response = client.get('/invalid')
    assert response.content_type == "application/json"
    data = response.get_json()
    assert data["status"] == 404


def test_metrics_endpoint(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert "cpu_percent" in data
    assert "memory_percent" in data
