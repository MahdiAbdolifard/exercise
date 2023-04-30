import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel1 = connection.channel()
channel1.queue_declare(queue='', durable=True)
channel1.exchange_declare(exchange='logs', exchange_type='fanout')
channel1.basic_publish(exchange='logs', routing_key='', body='hello word',
                        properties=pika.BasicProperties(headers={'name':'mahdi'}))
print('Sent massage.')
connection.close()