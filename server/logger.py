import logging
import logging.handlers
import json

class LogstashFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)
        return json.dumps({
            "@timestamp": record.created,
            "message": message,
            "level": record.levelname,
            "logger": record.name,
        })

# Logstash configuration
logstash_host = 'logstash'
logstash_port = 5044

# Create Logstash handler
logstash_handler = logging.handlers.SocketHandler(logstash_host, logstash_port)
logstash_handler.setFormatter(LogstashFormatter())
logstash_handler.setLevel(logging.INFO)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Configure root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logstash_handler)
logger.addHandler(console_handler)

# Test logging
logger.info("This is a test log message.")
