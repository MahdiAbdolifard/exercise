import pika 


connectoin = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connectoin.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue

binding_key = '*.*.notimpotant'

ch.queue_bind(queue=qname, exchange='topic_logs', routing_key=binding_key)
print('Waiting for message')

def callback(ch, method, properties, body):
    print(body)


ch.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)
ch.start_consuming()