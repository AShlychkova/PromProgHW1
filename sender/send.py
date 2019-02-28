from random import random
from time import sleep
import pika
sleep(10)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='hello')
while True:
    rand = random()
    print(rand)
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=str(rand))
    sleep(random())
connection.close()
