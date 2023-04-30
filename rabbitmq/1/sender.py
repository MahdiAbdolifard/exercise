import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel1 = connection.channel()

channel1.queue_declare(queue='queue_name')

channel1.basic_publish(exchange="", routing_key="queue_name", body="hi")

print(datetime.datetime.now())

connection.close()

