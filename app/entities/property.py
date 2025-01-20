from pydantic import BaseModel
from typing import List, Optional, Self, Type

from app.models.models import Property as PropertyModel

class Property(BaseModel):
    id: str
    sub_locality: str
    city: str
    street: str
    house_number: str
    complement: str
    postal_code: str
    pool: bool
    gourmet: bool
    grill: bool
    party_room: bool
    sports_court: bool
    gym: bool
    sauna: bool
    playground: bool
    gallery: Optional[List[dict]] = None
    type: str
    name: Optional[str] = None
    description: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    area: Optional[float] = None
    bedrooms: Optional[int] = None
    suites: Optional[int] = None
    bathrooms: Optional[int] = None
    parking_spaces: Optional[int] = None
    floor: Optional[int] = None
    price: Optional[float] = None
    condominium: Optional[float] = None
    iptu: Optional[float] = None
    
    @classmethod
    def from_orm(cls, property: Type[PropertyModel]) -> Self:
        return cls(
            id=property.id,
            sub_locality=property.sub_locality,
            city=property.city,
            street=property.street,
            house_number=property.house_number,
            complement=property.complement,
            postal_code=property.postal_code,
            pool=property.pool,
            gourmet=property.gourmet,
            grill=property.grill,
            party_room=property.party_room,
            sports_court=property.sports_court,
            gym=property.gym,
            sauna=property.sauna,
            playground=property.playground,
            gallery=property.gallery,
            type=property.type,
            name=property.name,
            description=property.description,
            phone=property.phone,
            email=property.email,
            area=property.area,
            bedrooms=property.bedrooms,
            suites=property.suites,
            bathrooms=property.bathrooms,
            parking_spaces=property.parking_spaces,
            floor=property.floor,
            price=property.price,
            condominium=property.condominium,
            iptu=property.iptu
        )

    def to_orm(self) -> PropertyModel:
        return PropertyModel(
            sub_locality=self.sub_locality,
            city=self.city,
            street=self.street,
            house_number=self.house_number,
            complement=self.complement,
            postal_code=self.postal_code,
            pool=self.pool,
            gourmet=self.gourmet,
            grill=self.grill,
            party_room=self.party_room,
            sports_court=self.sports_court,
            gym=self.gym,
            sauna=self.sauna,
            playground=self.playground,
            gallery=self.gallery,
            type=self.type,
            name=self.name,
            description=self.description,
            phone=self.phone,
            email=self.email,
            area=self.area,
            bedrooms=self.bedrooms,
            suites=self.suites,
            bathrooms=self.bathrooms,
            parking_spaces=self.parking_spaces,
            floor=self.floor,
            price=self.price,
            condominium=self.condominium,
            iptu=self.iptu
        )

    def to_dict(self, exclude: Optional[List[str]] = None) -> dict:
        if exclude is None:
            exclude = []

        property = {
            "data": {
            "id": self.id,
            "adress": {
                "subLocality": self.sub_locality,
                "city": self.city,
                "street": self.street,
                "houseNumber": self.house_number,
                "complement": self.complement,
                "postalCode": self.postal_code
            },
            "leisure": {
                "pool": self.pool,
                "gourmet": self.gourmet,
                "grill": self.grill,
                "partyRoom": self.party_room,
                "playground": self.playground,
                "sportsCourt": self.sports_court,
                "gym": self.gym,
                "sauna": self.sauna
            },
            "gallery": self.gallery,
            "type": self.type,
            "name": self.name,
            "description": self.description,
            "phone": self.phone,
            "email": self.email,
            "area": self.area,
            "bedrooms": self.bedrooms,
            "suites": self.suites,
            "bathrooms": self.bathrooms,
            "parkingSpaces": self.parking_spaces,
            "floor": self.floor,
            "price": self.price,
            "condominium": self.condominium,
            "iptu": self.iptu
            }
        }

        for key in exclude:
            property.pop(key, None)

        return property
