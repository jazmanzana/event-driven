import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    queue_name = "processing"
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        # todo: waits 15 seconds and publishes to "done" queue
        print(f"Was called with ch, method, properties, body: {ch} {method} {properties} {body}")

    channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
