import os
import pika
import json
from logger import get_logger


is_testing = os.environ["FLASK_ENV"] == "testing"

def get_connection():
    credentials = pika.PlainCredentials("guest", "guest")
    return pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq", credentials=credentials)
    )


class RabbitProducer:
    def __init__(self, queue_name):
        self.queue_name = queue_name
           
        if is_testing:
            return
        
        self.connection = get_connection()
        self.channel = self.connection.channel()
        self.logger = get_logger(f"rabbit_{queue_name}_producer")
        # Declare the queue in the constructor
        self.channel.queue_declare(queue=self.queue_name)

    def push_message(self, message):
        if os.environ["FLASK_ENV"] == "testing":
            return
        
        self.channel.basic_publish(
            exchange="", routing_key=self.queue_name, body=json.dumps(message)
        )
        print(f"Message pushed to {self.queue_name}: {message}")

    def close_connection(self):
        self.connection.close()


class RabbitConsumer:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        
        if is_testing:
            self.logger.info("Testing env. not consuming message")
            return
        
        self.connection = get_connection()
        self.channel = self.connection.channel()
        self.logger = get_logger(f"rabbit_{queue_name}_consumer")
        # Declare the queue in the constructor
        self.channel.queue_declare(queue=self.queue_name)

    def handle_message(self, callback_function):
        if is_testing:
            self.logger.info("Testing env. not consuming message")
            return
        
        def on_message(ch, method, properties, body):
            message = json.loads(body)
            callback_function(message, self.logger)

        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=on_message, auto_ack=True
        )
        print(f"Waiting for messages in {self.queue_name}...")
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()
