from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
import uuid
from . import Base

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(String(128), primary_key=True)
    firstName = Column(String(128))
    lastName = Column(String(128))
    email = Column(String(128))
    description = Column(String(128))
    occupation = Column(String(128))
    picture = Column(String(128), default='default.jpg')
    phoneNumber = Column(String(128))
    website = Column(String(128))
    property = relationship('Property', back_populates='profile')
    # nonce = relationship('Nonce', back_populates='profile')

    def __init__(self, **kwargs):
        """Initializes a new Profile"""
        super().__init__(**kwargs)
        self.id = kwargs.get('id', str(uuid.uuid4()))
        # self.picture = kwargs.get('picture', 'default.jpg')
        self.phoneNumber = kwargs.get('phoneNumber', '')
        self.website = kwargs.get('website', '')
        self.description = kwargs.get('description', '')
        self.occupation = kwargs.get('occupation', '')
        self.email = kwargs.get('email', '')
        self.lastName = kwargs.get('lastName', '')
        self.firstName = kwargs.get('firstName', '')