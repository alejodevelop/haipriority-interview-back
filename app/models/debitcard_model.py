from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class DebitCard(Base):
    __tablename__ = 'debit_cards'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    card_number = Column(String, unique=True, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    card_holder_name = Column(String, nullable=False)
    balance = Column(Float, default=0)
    creation_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="debit_cards")
