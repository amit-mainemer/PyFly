import pytest
from server.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_flights(client):
    response = client.get("/flights")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data["flights"]) > 0
    assert data["total"] > 0
    assert data["current_page"] == 1
