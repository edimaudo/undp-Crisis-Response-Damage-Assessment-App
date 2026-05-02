from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"])

def hash_pw(p): return pwd.hash(p)
def verify_pw(p, h): return pwd.verify(p, h)
