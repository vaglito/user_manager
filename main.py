import threading
from fastapi import FastAPI
from interfaces.api.routes import auth, users
from apps.users.infrastructure.models import Base
from config.db import engine
from adapters.consumers.user_create_consumer import start_consumer

app = FastAPI(title="Hexagonal FastAPI App")

@app.on_event("startup")
async def on_startup():
    # Crear tablas automáticamente
    Base.metadata.create_all(bind=engine)

    threading.Thread(target=start_consumer, daemon=True).start()
    print("RabbitMQ consumer started")

app.include_router(users.router)
app.include_router(auth.router)