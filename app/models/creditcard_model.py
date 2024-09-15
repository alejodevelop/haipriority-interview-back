from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CreditCard(Base):
    __tablename__ = 'credit_cards'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    card_number = Column(String, unique=True, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    card_holder_name = Column(String, nullable=False)
    credit_limit = Column(Float, nullable=False)
    balance = Column(Float, default=0)
    creation_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="credit_cards")
