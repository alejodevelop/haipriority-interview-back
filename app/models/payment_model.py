from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_type = Column(String, nullable=False)  # 'debit_card', 'credit_card', 'loan'
    product_id = Column(Integer, nullable=False)  # Id del producto específico
    payment_amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="payments")
