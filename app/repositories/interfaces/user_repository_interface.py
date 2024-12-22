from abc import ABC, abstractmethod


class IUserRepository(ABC):
    
    @abstractmethod
    def create_user(self, user: User) -> None:
        pass
