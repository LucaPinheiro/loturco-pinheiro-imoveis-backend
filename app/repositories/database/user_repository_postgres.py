from sqlalchemy.orm import Session
from app.entities.user import User
from app.repositories.interfaces.user_repository_interface import IUserRepository


class UserRepositoryPostgres(IUserRepository):
    def __init__(self, db: Session):
        self.db = db
        
    def create_user(self, user: User) -> None:
        user_orm = user.to_orm()
        self.db.add(user_orm)
        self.db.commit()
    

