from sqlalchemy.orm import Session
from app.entities.user import User
from app.repositories.interfaces.user_repository_interface import IUserRepository


class UserRepositoryPostgres(IUserRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def create_user(self, user: User) -> None:
        print(user,  " user no db postgres")
        user_orm = user.to_orm()
        print('*************')
        print(user_orm, " user_orm no db postgres")
        self.db.add(user_orm)
        print('*************')
        print(user_orm, " user_orm no db postgres foi adicionado")
        self.db.commit()
    

