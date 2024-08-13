import pytest
from test_app import app
from models import db, User
from mock import mock_user, second_mock_user, failed_password_mock_user



@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_users(client):
    # Add a user to the database
    test_user = User.query.filter_by(real_id=mock_user["real_id"]).first()
    if test_user is None:
        db.session.add(
            User(mock_user["full_name"], mock_user["password"], mock_user["real_id"])
        )
        db.session.commit()

    response = client.get("/users")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0


def test_create_user(client):
    # Happy Flow
    test_user = User.query.filter_by(real_id=second_mock_user["real_id"]).first()
    if test_user is not None:
        db.session.delete(test_user)
        db.session.commit()

    response = client.post("/users", json=second_mock_user)
    assert response.status_code == 200
    data = response.get_json()
    assert "newUserId" in data

    user = User.query.filter_by(id=data["newUserId"]).first()
    assert user is not None
    assert user.full_name == second_mock_user["full_name"]
    assert user.real_id == second_mock_user["real_id"]


def test_create_user_password_validation_error(client):
    response = client.post("/users", json=failed_password_mock_user)

    assert response.status_code == 422
    data = response.get_json()
    assert "messages" in data
    assert "password" in data["messages"]
