import bcrypt

from app.env import Env


class Encrypt:
    
    @staticmethod
    def hash_password(password: str) -> str:
        encrypt_key = Env.ENCRYPT_KEY.encode()
        return bcrypt.hashpw(password.encode(), encrypt_key).decode()
    
    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())