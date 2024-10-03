from pydantic import BaseModel, field_validator


class Profile(BaseModel):
    """Profile schema"""
    firstName: str
    lastName: str
    email: str
    description: str
    occupation: str
    picture: str
    phoneNumber: str
    website: str

    class Config:
        orm_mode = True

class ProfileResponse(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    description: str
    occupation: str
    phoneNumber: str
    website: str
    picture: str


class Property(BaseModel):
    """Property schema"""
    image: str
    title: str
    description: str
    price: str

    class Config:
        orm_mode = True

class Nonce(BaseModel):
    """Nonce schema"""
    nonce: str
    wallet_address: str

    class Config:
        orm_mode = True

class VerifySignatureRequest(BaseModel):
    wallet_address: str
    signature: str
    nonce: str

class JWTResponse(BaseModel):
    access_token: str