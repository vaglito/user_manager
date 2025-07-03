from fastapi import FastAPI
from interfaces.api.routes import users

app = FastAPI()
app.include_router(users.router)