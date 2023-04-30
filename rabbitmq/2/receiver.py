import pika 
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel2 = connection.channel()
channel2.queue_declare(queue='first', durable=True)
print('Wating for message, press ctrl+c to exit')


def callback(channel2, method, properties, body):
    print(f'Received {body}')
    print(properties.headers)
    time.sleep(9)
    print('Done...')
    channel2.basic_ack(delivery_tag=method.delivery_tag)


channel2.basic_qos(prefetch_count=1)
channel2.basic_consume(queue='first', on_message_callback=callback)


channel2.start_consuming()