from decouple import config, Csv

DB_CONNECT = {
    "engine": "postgresql",
    "user": config('POSTGRES_USER'),
    "password": config('POSTGRES_PASSWORD'),
    "db": config('POSTGRES_DB'),
    "host": config('POSTGRES_HOST', default='localhost'),
    "port": config('POSTGRES_PORT', default=5432, cast=int)
}

DB_URL = f"{DB_CONNECT['engine']}://{DB_CONNECT['user']}:{DB_CONNECT['password']}@{DB_CONNECT['host']}:{DB_CONNECT['port']}/{DB_CONNECT['db']}"

RABBITMQ_URL = config("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")