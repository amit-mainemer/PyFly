import requests
import json
from flask_seeder import Seeder
from server.models import Country
from server.logger import logger


class CountrySeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 5

    def run(self):
        logger.info("Seeding CountrySeeder")
        countries = Country.query.all()
        if len(countries) > 0:
            return

        res = requests.get(url="https://restcountries.com/v3.1/all")
        data = res.json()
        arr = json.loads(data)
        for country in arr:
            countryName = country["name"]["official"]
            country = Country(countryName, country["cca3"])
            self.db.session.add(country)
