import os 
from enum import Enum


class ENVIRONMENT:
    STAGE = os.environ.get('STAGE')
    AWS_ACCOUNT_ID = os.environ.get('AWS_ACCOUNT_ID')
    AWS_REGION = os.environ.get('AWS_REGION') or 'sa-east-1'
    STACK_NAME = os.environ.get('STACK_NAME')
    
    @classmethod
    def to_dict(cls):
        return {
            'STAGE': cls.STAGE,
            'AWS_ACCOUNT_ID': cls.AWS_ACCOUNT_ID,
            'STACK_NAME': cls.STACK_NAME
        }
        

class METHOD(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'