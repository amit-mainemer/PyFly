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

logstash_host = 'logstash'
logstash_port = 5044

logstash_handler = logging.handlers.SocketHandler(logstash_host, logstash_port)
logstash_handler.setFormatter(LogstashFormatter())
logstash_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logstash_handler)