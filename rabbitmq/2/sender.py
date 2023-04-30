import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel1 = connection.channel()
channel1.queue_declare(queue='first', durable=True)
massage = 'This is a testing massage'
channel1.basic_publish(exchange='', routing_key='first', body=massage,
                        properties=pika.BasicProperties(delivery_mode=True, headers={'name':'mahdi'}))
print('sent message.')
connection.close()

