import os
import threading
from app import create_app, db
from flask_migrate import Migrate, upgrade
from flask_seeder import FlaskSeeder
from flask_cors import CORS
from rabbit import RabbitConsumer
from constants import TICKETS_ORDER_QUEUE
from handlers.TicketOrderHandler import handle_new_order
from seeds.CountrySeeder import CountrySeeder
from seeds.FlightSeeder import FlightSeeder
from seeds.UserSeeder import UserSeeder

def create_app_instance():
    env = os.environ.get("FLASK_ENV", "development")
    
    if env != "production":
        db_uri = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@localhost:5433/{os.environ['POSTGRES_DB']}"
    else:
        db_uri = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@db:5432/{os.environ['POSTGRES_DB']}"

    app = create_app(db_uri)
    return app

def apply_migrations_and_seeders(app):
    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Apply migrations & seeders
    try:
        with app.app_context():
            app.logger.info("Applying database migrations...")
            upgrade()
            app.logger.info("Seeding the database")
            seeder = FlaskSeeder()
            seeder.init_app(app, db)
            seeders = [CountrySeeder(db=db), UserSeeder(db=db), FlightSeeder(db=db)]
            
            for seeder in seeders:
                seeder.run()
            
            db.session.commit()
                  
    except Exception as e:
        app.logger.error(f"Error during migration or seeding: {e}")
        raise

def start_consumers():
    consumer = RabbitConsumer(TICKETS_ORDER_QUEUE)
    consumer.handle_message(handle_new_order)
    
def main():
    app = create_app_instance()

    apply_migrations_and_seeders(app)
    
    consumer_thread = threading.Thread(target=start_consumers, daemon=True)
    consumer_thread.start()

    CORS(app)
    app.logger.info("Starting Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()
