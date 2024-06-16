import pika

class RabbitMQClient:
    def __init__(self, host='localhost', queue='log_queue'):
        self.host = host
        self.queue = queue
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue, durable=True)

    def send_message(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Faz com que a mensagem seja persistente
            )
        )
        print(f" [x] Enviado '{message}' para a fila '{self.queue}'")

    def close(self):
        if self.connection:
            self.connection.close()
