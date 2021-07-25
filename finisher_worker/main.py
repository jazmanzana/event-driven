import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    done_queue_name = "done"

    channel.queue_declare(queue=done_queue_name)

    def callback(ch, method, properties, body):
        # todo: calls my app via http
        print(f"Notification of done job: {body}")
        pass

    channel.basic_consume(done_queue_name, auto_ack=True, on_message_callback=callback)

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
