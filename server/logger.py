import os
import logging
import logging.handlers
from logstash_async.handler import AsynchronousLogstashHandler
import json

if os.environ["FLASK_ENV"] == "testing":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
else:
    logstash_host = "logstash"
    logstash_port = 5044

    class LogstashFormatter(logging.Formatter):
        def format(self, record):
            message = super().format(record)
            return json.dumps(
                {
                    "message": message,
                    "level": record.levelname,
                    "logger": record.name,
                }
            )

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.WARN)
    console_handler.setLevel(logging.ERROR)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.ERROR)
    logger.setLevel(logging.WARN)
    try:
        logstash_handler = AsynchronousLogstashHandler(
            logstash_host, logstash_port, database_path=None
        )
        logstash_handler.setFormatter(LogstashFormatter())
        logstash_handler.setLevel(logging.INFO)
        logstash_handler.setLevel(logging.DEBUG)
        logstash_handler.setLevel(logging.WARN)
        logstash_handler.setLevel(logging.ERROR)
        logger.addHandler(logstash_handler)
    except Exception as e:
        # Logstash handler failed to set up; log this error to console
        logger.error(f"Failed to set up Logstash handler: {e}")
        
    logger.addHandler(logstash_handler)
    logger.addHandler(console_handler)

    # Test logging
    logger.info("This is a test log message.")
