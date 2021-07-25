import pika


class Publisher:
    EXCHANGE = ""
    QUEUE = "processing"

    def __init__(self) -> None:
        self.connection = None
        self.channel = None

    def close_connection(self) -> None:
        self.connection.close()

    def connect(self, url="queues") -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=url))

    def open_channel(self) -> None:
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Publisher.QUEUE)

    def publish(self, body: str) -> None:
        # todo: handle error
        self.channel.basic_publish(exchange="", routing_key=Publisher.QUEUE, body=body)
