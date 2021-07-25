import pika


# todo: add typing
# todo: reuse connections
class Processing:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="queues"))  # todo: read from env
        self.channel = self.connection.channel()
        self.queue_name = "processing"
        self.channel.queue_declare(queue=self.queue_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def enqueue(self, body):
        # todo: handle error
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=body)
