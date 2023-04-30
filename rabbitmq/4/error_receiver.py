import pika


connction = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch2 = connction.channel()

ch2.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = ch2.queue_declare(queue='', exclusive=True)
qname = result.method.queue

serverity = 'info'

ch2.queue_bind(queue=qname, exchange='direct_logs', routing_key=serverity)

print('Waiting for massage')

def callback(ch2, method, properties, body):
    with open('error_logs.log', 'a') as el:
        el.write(str(body)+ '\n') 

ch2.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)
ch2.start_consuming()
