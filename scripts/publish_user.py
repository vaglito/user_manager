import pika
import json


def send_user_to_queue(user_data: dict, amqp_url="amqp://guest:guest@localhost:5672/", queue_name="create_user"):
    """
    Send user data to the specified RabbitMQ queue.

    Args:
        user_data (dict): Dictionary with user fields (email, password, etc.)
        amqp_url (str): RabbitMQ connection URL.
        queue_name (str): Queue name to send the message to.
    """
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
    channel = connection.channel()

    # Declare the queue (in case it doesn't exist)
    channel.queue_declare(queue=queue_name)

    # Publish the message
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(user_data)
    )

    print(f"✅ User sent to queue '{queue_name}': {user_data['email']}")
    connection.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Send user data to RabbitMQ.")
    parser.add_argument("--email", required=True, help="User email")
    parser.add_argument("--password", required=True, help="User password")
    parser.add_argument("--first_name", required=True, help="User first name")
    parser.add_argument("--last_name", required=True, help="User last name")
    parser.add_argument("--phone", required=True, help="User phone number")

    args = parser.parse_args()

    user_data = {
        "email": args.email,
        "password": args.password,
        "first_name": args.first_name,
        "last_name": args.last_name,
        "phone": args.phone
    }

    send_user_to_queue(user_data)