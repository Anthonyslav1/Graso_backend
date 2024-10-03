from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
import uuid

class Property(Base):
    """Property model of a user"""
    __tablename__ = 'properties'
    id = Column(String(128), primary_key=True)
    image = Column(String(128))
    title = Column(String(128))
    description = Column(String(128))
    price = Column(String(128))
    profile_id = Column(String(128), ForeignKey('profiles.id'))
    profile = relationship('Profile', back_populates='property')

    def __init__(self, **kwargs):
        """Initializes a new Property"""
        super().__init__(**kwargs)
        self.id = kwargs.get('id', '')
        self.image = kwargs.get('image', 'default.jpg')
        self.title = kwargs.get('title', '')
        self.description = kwargs.get('description', '')
        self.price = kwargs.get('price', '')