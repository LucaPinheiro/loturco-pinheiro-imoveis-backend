import os
from enum import Enum
from dotenv import load_dotenv


class StageEnum(Enum):
    PROD = "prod"
    HOM = "hom"
    DEV = "dev"
    TEST = "test"
    

class Env:
    load_dotenv()
    
    STAGE: StageEnum = os.environ.get("STAGE")
    
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    
    JWT_SECRET: str = os.environ.get("JWT_SECRET", 'secret')
    
    ENCRYPT_KEY: str = os.environ.get("ENCRYPT_KEY", '$2b$12$K2wnfHK/BhGEwMMMYPK9rO')