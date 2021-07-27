from worker.adapters.queues import Consumer, Publisher
from multiprocessing import Process
import time


def callback(ch, method, properties, body):
    del ch, method, properties
    time.sleep(20)
    publisher = Publisher()
    publisher.publish(body)


def consume() -> None:
    """
    Initializes a consumer for a given queue and
    executes the set callback function with the body of the consumed message.
    :return:
    """
    consumer = Consumer()
    consumer.set_callback(callback)
    consumer.start_consuming()


if __name__ == "__main__":
    """
    Starts two processes that ran a consumer each.
    """
    p1 = Process(target=consume)
    p1.start()
    p2 = Process(target=consume)
    p2.start()
    p1.join()
    p2.join()
