from pika.adapters.asyncio_connection import AsyncioConnection
import pika


# todo: add typing
class Consumer:
    EXCHANGE = ""
    QUEUE = "processing"

    def __init__(self):
        self.connection = None
        self.channel = None

    def connect(self, url="queues"):
        self.connection = AsyncioConnection(
            parameters=pika.URLParameters(url), on_open_callback=self.open_channel()
        )

    def close_connection(self):
        self.connection.close()

    def open_channel(self):
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Consumer.QUEUE)

    def start_consuming(self, callback):
        self.channel.basic_consume(
            queue=Consumer.QUEUE, auto_ack=True, on_message_callback=callback
        )
        self.channel.start_consuming()


class Publisher:
    EXCHANGE = ""
    QUEUE = "done"

    def __init__(self):
        self.connection = None
        self.channel = None

    def close_connection(self):
        self.connection.close()

    def connect(self, url="queues"):
        self.connection = AsyncioConnection(
            parameters=pika.URLParameters(url), on_open_callback=self.open_channel()
        )

    def open_channel(self):
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Publisher.QUEUE)

    def publish(self, body):
        self.channel.basic_publish(exchange="", routing_key=Publisher.QUEUE, body=body)
