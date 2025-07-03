import pika
import json
from apps.users.infrastructure.repositories import SQLAlchemyUserRepository
from apps.users.application.commands.create_user import CreateUserCommand, CreateUserUseCase

def callback(ch, method, properties, body):
    data = json.loads(body)
    repo = SQLAlchemyUserRepository()
    use_case = CreateUserUseCase(repo)
    command = CreateUserCommand(**data)
    use_case.execute(command)
    print("User created from RabbitMQ")

def start_consumer():
    connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@rabbitmq:5672/"))
    channel = connection.channel()
    channel.queue_declare(queue='create_user')
    channel.basic_consume(queue='create_user', on_message_callback=callback, auto_ack=True)
    print("Waiting for create_user messages...")
    channel.start_consuming()