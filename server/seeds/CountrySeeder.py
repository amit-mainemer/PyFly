from flask_seeder import Seeder
from models import Country
from logger import logger
import requests
import numpy as np



class CountrySeeder(Seeder):
  def __init__(self, db=None):
    super().__init__(db=db)
    self.priority = 10

  def run(self):
    logger.info("Seeding CountrySeeder")
    countries = Country.query.all()
    if len(countries) > 0:
        return
      
    res = requests.get(url = "https://restcountries.com/v3.1/all")
    data = res.json()
    arr = np.array(data)
    for country in arr[50:100]:
        countryName = country['name']['official']
        logger.debug(countryName)
        country = Country(countryName)
        self.db.session.add(country)
