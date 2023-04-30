import pika
import uuid
from random import randint


class Sender():
    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.ch = self.connection.channel()
        result = self.ch.queue_declare(queue='', exclusive=True)
        self.qname = result.method.queue
        self.ch.basic_consume(queue=self.qname, on_message_callback=self.on_response, auto_ack=True)

    def on_response(self, ch, method, proper, body):
        if self.corr_id == proper.correlation_id:
            self.respons = body


    def call(self, number:int):
        self.respons = None
        self.corr_id = str(uuid.uuid4())
        send.ch.basic_publish(exchange='', routing_key='rpc_queue',
                    properties=pika.BasicProperties(headers={'name_client':'client_two'}, reply_to=self.qname,
                                    correlation_id=self.corr_id,), body=str(number))
        print(f'Number {num} was sent')
        while self.respons is None:
            self.connection.process_data_events()
        return int(self.respons)


send = Sender()
num = randint(0, 100)
rexponse = send.call(num)

print(f'The response received from the server : {rexponse}')