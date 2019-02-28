import pika
import sys
from time import sleep
sleep(10)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("%r" % body)
    sys.stdout.flush()

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
