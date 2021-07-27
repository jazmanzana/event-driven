from collections.abc import Callable
import pika
import os


class Publisher:
    EXCHANGE = ""
    QUEUE = "processing"

    def __init__(self, url="queues"):
        # this type of connection is affecting my performance
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Publisher.QUEUE)
        self.properties = pika.BasicProperties(expiration=os.getenv("JOB_EXPIRATION", default="60000"))

    def publish(self, body: bytes):
        self.channel.basic_publish(
            exchange="", routing_key=Publisher.QUEUE, body=str(body), properties=self.properties
        )


class Consumer:
    EXCHANGE = ""
    QUEUE = "done"

    def __init__(self, url="queues"):
        # this type of connection is affecting my performance
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Consumer.QUEUE)

    def set_callback(self, callback: Callable):
        self.channel.basic_consume(
            queue=Consumer.QUEUE, auto_ack=False, on_message_callback=callback
        )

    def start_consuming(self):
        self.channel.start_consuming()

    def acknowledge_message(self):
        self.channel.basic_ack(Consumer.QUEUE)
