import boto3, uuid
from app.core.config import settings

s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_KEY,
    aws_secret_access_key=settings.AWS_SECRET
)

def upload_image(file):
    key = f"reports/{uuid.uuid4()}.jpg"
    s3.upload_fileobj(file, settings.BUCKET, key)
    return f"{settings.CDN_URL}/{key}"
