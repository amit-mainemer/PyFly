from flask_seeder import Seeder
import random
from datetime import datetime, timedelta
from models import Flight, Country
from schemas import country_to_dict
from logger import get_logger



def get_random_time_this_week():
    now = datetime.now()
    start_of_week = now - timedelta(days=now.weekday())
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)
    random_timestamp = random.randint(
        int(start_of_week.timestamp()), int(end_of_week.timestamp())
    )
    random_datetime = datetime.fromtimestamp(random_timestamp)
    return random_datetime


class FlightSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10
        self.logger = get_logger("flight_seeder")

    def run(self):
        self.logger.info("Seeding FlightSeeder")
        flights = Flight.query.all()
        if len(flights) > 0:
            self.logger.info("Exiting FlightSeeder. data exists")
            return
        countries = Country.query.all()
        countries_dicts = [country_to_dict(country) for country in countries]
        for index, country in enumerate(countries_dicts):
            if int(index) + 1 == len(countries):
                break

            newFlight = Flight(
                50,
                country["id"],
                countries_dicts[int(index) + 1]["id"],
                get_random_time_this_week(),
            )
            self.db.session.add(newFlight)
