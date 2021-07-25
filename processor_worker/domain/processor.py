from processor_worker.adapters.queues import Consumer, Publisher
import time


def callback(ch, method, properties, body: str) -> None:
    del ch, method, properties
    # waits 20 seconds and publishes to "done" queue
    time.sleep(20)
    publisher = Publisher.connect()
    publisher.publish(body)


def consume() -> None:
    consumer = Consumer().connect()
    consumer.start_consuming(callback())
