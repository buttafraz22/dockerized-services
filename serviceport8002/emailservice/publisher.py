# import pika, json

# params=pika.ConnectionParameters('localhost')

# conection=pika.BlockingConnection(params)

# channel=conection.channel()

# def publish(method,body):
#     properties=pika.BasicProperties(method)
#     channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
# import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

# def publish(body):

#     channel.queue_declare(queue='hello')
#     channel.basic_publish(exchange='',
#                         routing_key='hello',
#                         body=body)
# connection.close()

import pika



def publish(body):
    params=pika.URLParameters('amqps://xssqkxjm:hFarJn9pkK-1d-auj-q4J90958WKoSox@fly.rmq.cloudamqp.com/xssqkxjm')

    connection=pika.BlockingConnection(params)
    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='main')
    channel.basic_publish(exchange='',
                        routing_key='main',
                        body=body)
    