import re
from pydantic import BaseModel, field_validator

from app.constants import Constants


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    
    @field_validator("email", mode='after')
    def validate_email(cls, value):
        assert re.match(Constants.REGEX_EMAIL, value), "email must be a valid email"
        return value
    