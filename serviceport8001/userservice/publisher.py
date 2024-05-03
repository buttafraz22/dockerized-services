# import pika, json

# params=pika.URLParameters('amqps://xssqkxjm:hFarJn9pkK-1d-auj-q4J90958WKoSox@fly.rmq.cloudamqp.com/xssqkxjm')

# conection=pika.BlockingConnection(params)

# channel=conection.channel()

# def publish(method,body):
#     properties=pika.BasicProperties(method)
#     channel.basic_publish(exchange='', routing_key='admin', body=json.dump(body), properties=properties)

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
    
