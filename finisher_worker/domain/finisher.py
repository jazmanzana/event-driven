from finisher_worker.adapters.queues import Consumer


# todo: add typing
def callback(ch, method, properties, body):
    # todo: calls my app via http
    print(f"Notification of done job: {body}")


def consume():
    consumer = Consumer().connect()
    consumer.start_consuming(callback())
