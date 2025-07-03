import pika
import json
from apps.users.infrastructure.repositories import SQLAlchemyUserRepository
from apps.users.application.commands.create_user import CreateUserCommand, CreateUserUseCase

def callback(ch, method, properties, body):
    """
    Callback function that is triggered whenever a message is received 
    from the 'create_user' queue.

    This function parses the message body, instantiates the use case, 
    and executes the user creation logic.

    Args:
        ch: The channel object.
        method: Method frame with delivery information.
        properties: Message properties.
        body: The actual message body in bytes (expected to be JSON).
    """
    data = json.loads(body)
    repo = SQLAlchemyUserRepository()
    use_case = CreateUserUseCase(repo)
    command = CreateUserCommand(**data)
    use_case.execute(command)
    print("User created from RabbitMQ")

def start_consumer():
    """
    Starts the RabbitMQ consumer for the 'create_user' queue.

    This function establishes a connection with the RabbitMQ server,
    declares the queue (in case it doesn't exist), and begins 
    consuming messages using the `callback` function.
    """
    connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@rabbitmq:5672/"))
    channel = connection.channel()
    channel.queue_declare(queue='create_user')
    channel.basic_consume(queue='create_user', on_message_callback=callback, auto_ack=True)
    print("Waiting for create_user messages...")
    channel.start_consuming()