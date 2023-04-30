import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel2 = connection.channel()

channel2.queue_declare(queue='queue_name')

def callbake(ch, method, properties, body):
    print(f'Received {body}.')


channel2.basic_consume(queue='queue_name', on_message_callback=callbake, auto_ack=True)

print("Waiting for massage, to exit press ctrl+c")

channel2.start_consuming()