import os
from flask.cli import FlaskGroup
from server.application import create_app

def create_app_with_config():
    env = os.environ.get("FLASK_ENV", "development")
    if env != "production":
        db_uri = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@localhost:5433/{os.environ['POSTGRES_DB']}"
    else:
        db_uri = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@db:5432/{os.environ['POSTGRES_DB']}"

    return create_app(db_uri=db_uri)

cli = FlaskGroup(create_app=create_app_with_config)

if __name__ == "__main__":
    cli()