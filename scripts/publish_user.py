
import pika
import json

# Datos del nuevo usuario
user_data = {
    "email": "cesar@example.com",
    "password": "mypassword123",
    "first_name": "César",
    "last_name": "Gonzalez",
    "phone": "987654321"
}

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@localhost:5672/"))
channel = connection.channel()

# Declarar la cola (por si no existe)
channel.queue_declare(queue='create_user')

# Enviar mensaje
channel.basic_publish(
    exchange='',
    routing_key='create_user',
    body=json.dumps(user_data)
)

print("Usuario enviado a RabbitMQ")
connection.close()
