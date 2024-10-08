from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

CASCADE_OPTION = "all, delete-orphan"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    creation_date = Column(DateTime, nullable=False)

    debit_cards = relationship("DebitCard", back_populates="user", cascade=CASCADE_OPTION)
    credit_cards = relationship("CreditCard", back_populates="user", cascade=CASCADE_OPTION)
    loans = relationship("Loan", back_populates="user", cascade=CASCADE_OPTION)
    audit_logs = relationship("AuditLog", back_populates="user", cascade=CASCADE_OPTION)
