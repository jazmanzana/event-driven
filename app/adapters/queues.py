import pika


# todo: add typing
class Publisher:
    EXCHANGE = ""
    QUEUE = "processing"

    def __init__(self):
        self.connection = None
        self.channel = None

    def close_connection(self):
        self.connection.close()

    def connect(self, url):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="queues"))

    def open_channel(self):
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Publisher.QUEUE)

    def enqueue(self, body):
        # todo: handle error
        self.channel.basic_publish(exchange='', routing_key=Publisher.QUEUE, body=body)
