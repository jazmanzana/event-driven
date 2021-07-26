from worker.adapters.queues import Consumer, Publisher
from multiprocessing import Process
import time


def callback(ch, method, properties, body):
    del ch, method, properties
    time.sleep(20)
    publisher = Publisher()
    publisher.publish(body)


def consume():
    consumer = Consumer()
    consumer.set_callback(callback)
    consumer.start_consuming()


if __name__ == "__main__":
    p1 = Process(target=consume)
    p1.start()
    p2 = Process(target=consume)
    p2.start()
    p1.join()
    p2.join()
