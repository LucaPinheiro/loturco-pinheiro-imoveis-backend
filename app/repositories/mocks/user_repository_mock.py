from app.entities.user import User
from app.repositories.interfaces.user_repository_interface import IUserRepository

from app.helpers.encrypt import Encrypt


class UserRepoMock(IUserRepository):
    def __init__(self):
        self.users = [
            User(
                id="1",
                name='Luca Pinheiro',
                email='lucapgomes11@gmail.com',
                password=Encrypt.hash_password('123456')
            ),
            User(
                id="2",
                name='Yuri Drapack',
                email='yuridrapack@gmail.com',
                password=Encrypt.hash_password('123456')
            )   
        ]
        
    def create_user(self, user: User) -> None:
        self.users.append(user)