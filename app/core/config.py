import os

class Settings:
    ENV = os.getenv("ENV", "dev")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./crisis.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "change")
    AWS_KEY = os.getenv("AWS_KEY")
    AWS_SECRET = os.getenv("AWS_SECRET")
    BUCKET = os.getenv("BUCKET")
    CDN_URL = os.getenv("CDN_URL", "")

settings = Settings()
