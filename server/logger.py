import os
import logging
import logging.handlers
from logstash_async.handler import AsynchronousLogstashHandler
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set the default log level

if os.getenv("FLASK_ENV") == "testing":
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    
    logger.addHandler(console_handler)
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
                    "time": self.formatTime(record),
                }
            )

    # Console handler setup
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    logger.addHandler(console_handler)

    try:
        # Logstash handler setup
        logstash_handler = AsynchronousLogstashHandler(
            logstash_host, logstash_port, database_path=None
        )
        logstash_handler.setFormatter(LogstashFormatter())
        logstash_handler.setLevel(logging.INFO)
        
        logger.addHandler(logstash_handler)
        
        logger.info("Logstash handler successfully set up.")
    except Exception as e:
        logger.error(f"Failed to set up Logstash handler: {e}")

# Test logging
logger.info("This is a test log message.")
