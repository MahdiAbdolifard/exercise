import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

messages = {
    'error.warning.important':'This is an important messges',
    'info.debug.notimpotant':'This is not important messages'
}

for k,v in messages.items():
    ch.basic_publish(exchange='topic_logs', routing_key=k, body=v)

print('Sent')

connection.close()