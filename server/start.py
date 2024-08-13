import os
from app import create_app
from logger import logger


if __name__ == "__main__":
    env = os.environ.get("FLASK_ENV", "development")
    logger.info(f"flask_env: {env}")

    if env != "production":
        db_uri = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@localhost:5433/{os.environ['POSTGRES_DB']}"
    else:
        db_uri = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@db:5432/{os.environ['POSTGRES_DB']}"

    app = create_app(db_uri)
    app.run(host='0.0.0.0', port=5000, debug=True)
