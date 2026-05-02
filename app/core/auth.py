from jose import jwt
from datetime import datetime, timedelta
from app.core.config import settings

def create_token(user_id):
    return jwt.encode(
        {"sub": user_id, "exp": datetime.utcnow()+timedelta(minutes=30)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )
