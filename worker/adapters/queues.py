from collections.abc import Callable
import pika


class Publisher:
    EXCHANGE = ""
    QUEUE = "done"

    def __init__(self, url="localhost"):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Publisher.QUEUE)

    #def __exit__(self, exc_type, exc_value, traceback):
    #    self.connection.close()

    def publish(self, body: bytes):
        self.channel.basic_publish(exchange="", routing_key=Publisher.QUEUE, body=body)


class Consumer:
    EXCHANGE = ""
    QUEUE = "processing"

    def __init__(self, url="localhost"):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Consumer.QUEUE)

    #def __exit__(self, exc_type, exc_value, traceback):
    #    self.connection.close()

    def set_callback(self, callback: Callable):
        self.channel.basic_consume(
            queue=Consumer.QUEUE, auto_ack=False, on_message_callback=callback
        )

    def start_consuming(self):
        self.channel.start_consuming()

    def acknowledge_message(self):
        self.channel.basic_ack(Consumer.QUEUE)
