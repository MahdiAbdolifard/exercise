import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch1 = connection.channel()

ch1.exchange_declare(exchange='direct_logs', exchange_type='direct')

massage = {
    'info' : 'This is INFO massage.', 
    'error' : 'This is ERROR massage', 
    'warning' : 'This is WARNING massage', 
}

for k,v in massage.items():
    ch1.basic_publish(exchange='direct_logs', routing_key=k, body=v)

connection.close()

