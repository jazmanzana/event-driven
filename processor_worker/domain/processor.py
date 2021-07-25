from processor_worker.adapters.queues import Consumer, Publisher
import time


# todo: add typing
def callback(ch, method, properties, body):
    # waits 20 seconds and publishes to "done" queue
    time.sleep(20)
    publisher = Publisher.connect()
    publisher.publish(body)


def consume():
    consumer = Consumer().connect()
    consumer.start_consuming(callback())
