from sqlalchemy.orm import Session
from app.models.payment_model import Payment


class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payment: Payment):
        try:
            self.db.add(payment)
            self.db.commit()
            self.db.refresh(payment)
            return payment
        except:
            self.db.rollback()
            raise

    def get_by_user_id(self, user_id: int) -> Payment:
        return self.db.query(Payment).filter(Payment.user_id == user_id).first()
