from sqlalchemy import create_engine
from app.env import Env
from app.models.models import Base, User, Property


def create_db_tables():
    """Create database tables using SQLAlchemy."""
    try:
        engine = create_engine(Env.DATABASE_URL)

        print(f"Connecting to database at: {Env.DATABASE_URL}")
        print("Tables registered in Base.metadata:", Base.metadata.tables.keys())

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        print("Tables created successfully.")
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")


if __name__ == "__main__":
    create_db_tables()
