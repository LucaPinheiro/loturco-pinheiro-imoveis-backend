
from sqlalchemy import NullPool, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

import os

from app.helpers.exceptions import DatabaseException

from app.env import Env, StageEnum
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.repositories.mocks.user_repository_mock import UserRepoMock


class Repository:
    user_repo: IUserRepository
    
    def __init__(
        self, 
        user_repo: bool = False
    ):
        self.session = None
        
        if Env.STAGE == StageEnum.TEST:
            self._initialize_mock_repositories(user_repo)
        else:
            self._initialize_real_repositories(user_repo)
            
            
            
    def _initialize_mock_repositories(self, user_repo):
        if user_repo:
            self.user_repo = UserRepoMock()

    def _initialize_real_repositories(self, user_repo):
        if user_repo:
            self.session = self.__connect_db()

            
    def close_session(self):
        if self.session:
            self.session.close()
            self.session = None

    @staticmethod
    def __connect_db() -> Session:
        try:
            engine = create_engine(Env.DATABASE_URL, poolclass=NullPool)
            return Session(engine)  
        except (SQLAlchemyError, Exception) as error:
            raise DatabaseException(f"Database connection error: {error}")

    def __del__(self):
        self.close_session()
        
    def test_connection(self):
        return self.__connect_db()
            
if __name__ == "__main__":
    print(f"STAGE: {os.getenv('STAGE')}")
    print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
    print(f"JWT_SECRET: {os.getenv('JWT_SECRET')}")
    print(f"ENCRYPT_KEY: {os.getenv('ENCRYPT_KEY')}")

    try:
        repo = Repository()
        print(repo.test_connection())
        
    except Exception as e:
        print(e)