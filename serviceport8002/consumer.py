import pika, sys, os


def main():
    params=pika.URLParameters('amqps://xssqkxjm:hFarJn9pkK-1d-auj-q4J90958WKoSox@fly.rmq.cloudamqp.com/xssqkxjm')

    connection=pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue='main')

    def callback(ch, method, properties, body):
        print(f" [UserService] Received {body}")

    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
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