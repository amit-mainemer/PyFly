import os
import redis
from logger import logger

env = os.environ["FLASK_ENV"]

if env != "production":
    redis_host = "localhost"
else:
    redis_host = "redis"

redis_port = 6379

logger.info(f"Connecting to Redis at {redis_host}:{redis_port}")

try:
    redis_client = redis.StrictRedis(
        host=redis_host, port=redis_port, decode_responses=True
    )
    # Test the connection
    redis_client.ping()
    logger.info("Connected to Redis successfully.")
except redis.ConnectionError as e:
    logger.error(f"Failed to connect to Redis: {e}")
