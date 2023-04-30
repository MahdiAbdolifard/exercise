import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel2 = connection.channel()

channel2.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel2.queue_declare(queue='', exclusive=True)
qname = result.method.queue

channel2.queue_bind(queue=qname, exchange='logs')
print('Waiting for logs')

def callback(channel2, method, properties, body):
    print(f'Received {body}')
    print(properties.headers)
    print(qname)
channel2.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)
channel2.start_consuming()