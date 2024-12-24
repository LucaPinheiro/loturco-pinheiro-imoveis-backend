from sqlalchemy import create_engine
from app.env import Env
from app.models.models import Base


def create_db_tables():
    """Create database tables using SQLAlchemy."""
    try:
        engine = create_engine(Env.DATABASE_URL)

        Base.metadata.create_all(engine)

        print("Tables created successfully.")
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
        
if __name__ == "__main__":
    create_db_tables()