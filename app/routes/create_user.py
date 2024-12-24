import os
import uuid
from app.entities.user import User
from app.schema.http import HTTPError, HTTPRequest, HTTPResponse
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.repositories.repository import Repository
from app.schema.create_user import CreateUserRequest


class UseCase:
    repository: Repository
    user_repo: IUserRepository 
    
    def __init__(self):
        self.repository = Repository(user_repo=True)
        self.user_repo = self.repository.user_repo
    
    def execute(self, schema: CreateUserRequest):
        id = uuid.uuid4().hex
        user = User(
            id=id,
            name=schema.name,
            email=schema.email,
            password=schema.password
        )
        user = self.user_repo.create_user(user)

class Controller:
    @staticmethod
    def handle(request: HTTPRequest) -> HTTPResponse:
        use_case = None
        
        try:
            schema = CreateUserRequest(**request.body)
            print(schema)
            use_case = UseCase()
            use_case.execute(schema)
            
            return HTTPResponse(status_code=201, message="Usuário criado com sucesso!")
        
        except Exception as e:
            error_message = str(e)
            return HTTPError(status_code=500, details=error_message)
        
        
def lambda_handler(event, context):
    request = HTTPRequest(event)
    response = Controller.handle(request)
    
    return response.to_dict()



# Exemplo de teste local da rota

import json

if __name__ == "__main__":
    event = {
        "body": json.dumps({
            "name": "Lucão",
            "email": "luca@email.com",
            "password": "securepassword123"
        })
    }
    context = {}
    response = lambda_handler(event, context)
    print('foi!')
    print(response)
