from sqlalchemy import Column, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Boolean, Float, Integer, JSON


class Base(DeclarativeBase):
    __abstract__ = True

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"
    
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)


class Property(Base):
    __tablename__ = "properties"

    id = Column(String, primary_key=True, index=True)
    sub_locality = Column(String, nullable=False)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    house_number = Column(String, nullable=False)
    complement = Column(String)
    postal_code = Column(String, nullable=False)
    pool = Column(Boolean, default=False)
    gourmet = Column(Boolean, default=False)
    grill = Column(Boolean, default=False)
    party_room = Column(Boolean, default=False)
    sports_court = Column(Boolean, default=False)
    gym = Column(Boolean, default=False)
    sauna = Column(Boolean, default=False)
    playground = Column(Boolean, default=False)
    gallery = Column(JSON)
    type = Column(String, nullable=False)
    name = Column(String)
    description = Column(String)
    phone = Column(String)
    email = Column(String)
    area = Column(Float)
    bedrooms = Column(Integer)
    suites = Column(Integer)
    bathrooms = Column(Integer)
    parking_spaces = Column(Integer)
    floor = Column(Integer)
    price = Column(Float)
    condominium = Column(Float)
    iptu = Column(Float)