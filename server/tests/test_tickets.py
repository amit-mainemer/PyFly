import pytest
from test_app import (
    app,
)
from models import db, Flight, User, Country, Ticket
from mock import mock_flight, mock_user, mock_country, mock_country2
from logger import logger

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def country_setup(name, code):
    test_country = Country.query.filter_by(code=code).first()
    if test_country is None:
        test_country = Country(name, code)
        db.session.add(test_country)
        db.session.commit()

    return test_country


def flight_setup(seats):
    origin_country = country_setup(mock_country["name"], mock_country["code"])
    dest_country = country_setup(mock_country2["name"], mock_country2["code"])

    logger.debug("flight setup")
    logger.debug(origin_country.id)
    logger.debug(dest_country.id)

    test_flight = Flight.query.filter_by(dest_country_id=dest_country.id).first()
    if test_flight is None:
        test_flight = Flight(
            seats, origin_country.id, dest_country.id, mock_flight["date"]
        )
        db.session.add(test_flight)
        db.session.commit()
    else:
        test_flight.remaining_seats = seats
        db.session.commit()

    return test_flight


def user_setup():
    test_user = User.query.filter_by(real_id=mock_user["real_id"]).first()
    if test_user is None:
        test_user = User(
            mock_user["full_name"], mock_user["password"], mock_user["real_id"]
        )
        db.session.add(test_user)
        db.session.commit()

    return test_user


def test_buy_ticket(client):
    test_flight = flight_setup(2)
    test_user = user_setup()
    # buy flight ticket

    ticket_form = {
        "user_id": test_user.id,
        "flight_id": test_flight.id,
    }

    test_ticket = Ticket.query.filter_by(
        user_id=test_user.id, flight_id=test_flight.id
    ).first()
    if test_ticket is not None:
        db.session.delete(test_ticket)
        db.session.commit()

    response = client.post("/tickets", json=ticket_form)
    data = response.get_json()
    assert response.status_code == 200
    assert data["newTicketId"] is not None


def test_buy_ticket_no_seats(client):
    test_flight = flight_setup(0)
    test_user = user_setup()
    ticket_form = {
        "user_id": test_user.id,
        "flight_id": test_flight.id,
    }
    response = client.post("/tickets", json=ticket_form)
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "flight has no remaining seats"
