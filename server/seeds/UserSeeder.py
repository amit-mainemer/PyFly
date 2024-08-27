from faker import Faker
from flask_seeder import Seeder
from models import User
from logger import get_logger

fake = Faker()

class UserSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1
        self.logger = get_logger("user_seeder")

    def run(self):
        self.logger.info("Seeding UserSeeder")
        users = User.query.all()
        if len(users) > 0:
            self.logger.info("Exiting UserSeeder. data exists")
            return

        for i in range(0, 50):
            user = User(fake.name(), fake.password(), i + 1000)
            self.db.session.add(user)
