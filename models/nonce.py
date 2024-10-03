from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
import uuid

class Nonce(Base):
    """Nonce model of a user"""
    __tablename__ = 'nonces'
    id = Column(String(128), primary_key=True)
    nonce = Column(String(128))
    wallet_address = Column(String(128))
    # profile_id = Column(String(128), ForeignKey('profiles.id'))
    # profile = relationship('Profile', backref='nonce')

    def __init__(self, **kwargs):
        """Initializes a new Nonce"""
        super().__init__(**kwargs)
        self.id = str(uuid.uuid4())
        self.nonce = kwargs.get('nonce', '')
        self.wallet_address = kwargs.get('wallet_address', '')