from finisher_worker.adapters.queues import Consumer


def callback(ch, method, properties, body: str) -> None:
    del ch, method, properties
    # todo: calls my app via http
    print(f"Notification of done job: {body}")


def consume() -> None:
    Consumer().connect().start_consuming(callback())
