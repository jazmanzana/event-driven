import pika
# todo: add typing


class Adapter:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()


class Publisher(Adapter):
    def __init__(self):
        super().__init__(self)
        self.queue_name = "done"
        self.channel.queue_declare(queue=self.queue_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # todo: check good practices
        self.connection.close()

    def enqueue(self, job):
        # todo: put this in a try catch statement
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=job
        )


class Subscriber(Adapter):
    def __init__(self):
        super().__init__(self)
        self.queue_name = "processing"
        self.channel.basic_consume(
            queue=self.queue_name,
            auto_ack=True,
            on_message_callback=self.callback
        )
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print(f"Was called with ch, method, properties, body: {ch} {method} {properties} {body}")
        # todo: call domain, que hace un wait y luego escribe en la cola de done
