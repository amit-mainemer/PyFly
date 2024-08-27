import requests
import json
from flask_seeder import Seeder
from models import Country
from logger import get_logger


class CountrySeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 5
        self.logger = get_logger()

    def run(self):
        self.logger.info("Seeding CountrySeeder")
        countries = Country.query.all()
        if len(countries) > 0:
            self.logger.info("Existing CountrySeeder. data exists")
            return

        res = requests.get(url="https://restcountries.com/v3.1/all")
        data = res.json()
        for country in data:
            countryName = country["name"]["official"]
            country = Country(countryName, country["cca3"])
            self.db.session.add(country)
