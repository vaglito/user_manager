from scripts.publish_user import send_user_to_queue

user = {
    "email": "cesargonzalez390@gmail.com",
    "password": "Tel.domasclideo001",
    "first_name": "Cesar",
    "last_name": "Gonzalez",
    "phone": "999999999"
}

send_user_to_queue(user)