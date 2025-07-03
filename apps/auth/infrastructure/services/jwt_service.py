import jwt
from decouple import config
from datetime import datetime, timedelta
from apps.users.domain.entities import User

# Load environment configuration
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM', default='HS256')

class JWTService:
    """
    Service responsible for generating and decoding JSON Web Tokens (JWT).

    This service provides functionality to create secure tokens for user authentication
    and to decode and verify those tokens during protected requests.

    Methods:
        create_token(user: User) -> str:
            Generates a JWT token containing the user's UUID and email, with a 1-hour expiration time.

        decode_token(token: str) -> dict:
            Decodes and validates a given JWT token using the SECRET_KEY and ALGORITHM.
    """

    def create_token(self, user: User) -> str:
        """
        Create a JWT token for the given user.

        Args:
            user (User): The user entity for which to generate the token.

        Returns:
            str: Encoded JWT string containing user information.
        """
        payload = {
            "sub": str(user.uuid),
            "exp": datetime.now() + timedelta(hours=1),
            "email": user.email,
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    def decode_token(self, token: str) -> dict:
        """
        Decode and verify a JWT token.

        Args:
            token (str): The JWT string to decode.

        Returns:
            dict: The decoded payload containing user information.

        Raises:
            jwt.ExpiredSignatureError: If the token has expired.
            jwt.InvalidTokenError: If the token is invalid or tampered.
        """
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
