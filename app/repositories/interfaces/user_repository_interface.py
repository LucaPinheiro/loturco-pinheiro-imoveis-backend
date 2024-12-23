from abc import ABC, abstractmethod

from app.entities.user import User


class IUserRepository(ABC):
    
    @abstractmethod
    def create_user(self, user: User) -> None:
        pass
