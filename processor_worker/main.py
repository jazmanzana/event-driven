import pika, sys, os, time


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    processing_queue_name = "processing"
    done_queue_name = "done"

    channel.queue_declare(queue=processing_queue_name)
    channel.queue_declare(queue=done_queue_name)

    def callback(ch, method, properties, body):
        # todo: waits 20 seconds and publishes to "done" queue
        time.sleep(20)
        channel.basic_publish(exchange='', routing_key=done_queue_name, body=body)

    channel.basic_consume(queue=processing_queue_name, auto_ack=True, on_message_callback=callback)

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
