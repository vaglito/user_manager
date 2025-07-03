import jwt
from decouple import config, Csv
from datetime import datetime, timedelta
from apps.users.domain.entities import User

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM', default='HS256')

class JWTService:
    def create_token(self, user: User) -> str:
        payload = {
            "sub": str(user.uuid),
            "exp": datetime.now() + timedelta(hours=1),
            "email": user.email,
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    def decode_token(self, token: str) -> dict:
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

