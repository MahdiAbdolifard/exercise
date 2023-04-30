import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch1 = connection.channel()

ch1.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = ch1.queue_declare(queue='', exclusive=True)
qname = result.method.queue

serverities = ('info', 'error', 'warning')

for serverity in serverities:
    ch1.queue_bind(exchange='direct_logs', queue=qname, routing_key=serverity)
    '''
    روتین کی برای این است که بفهمه کدوم کلید هارو برداره و بخونه
      که ما هر بار چرخشی براش مشخص میکنیم 
    '''

print('Waiting for massage')

def callback(ch1, method, peroperties, body):
    print(f'{method.routing_key}, {body}')

ch1.basic_consume(queue=qname, on_message_callback=callback , auto_ack=True)

ch1.start_consuming()