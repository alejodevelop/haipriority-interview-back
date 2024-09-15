from typing import List

from sqlalchemy import inspect
from sqlalchemy.orm import Session
from app.models.loan_model import Loan


class LoanRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, loan: Loan):
        try:
            self.db.add(loan)
            self.db.commit()
            self.db.refresh(loan)
            return loan
        except:
            self.db.rollback()
            raise

    def get_by_user_id(self, user_id: int) -> List[Loan]:
        return self.db.query(Loan).filter(Loan.user_id == user_id).all()

    def get_by_loan_id(self, loan_id: int) -> Loan:
        return self.db.query(Loan).filter(Loan.id == loan_id).first()

    def update(self, loan_id: int, loan: Loan, user_id: int):
        try:
            loan_columns = {c.key for c in inspect(Loan).mapper.column_attrs}

            update_data = {key: value for key, value in loan.__dict__.items() if
                           key in loan_columns and value is not None}

            self.db.query(Loan).filter(
                Loan.id == loan_id and Loan.user_id == user_id).update(update_data)
            self.db.commit()
            return loan
        except:
            self.db.rollback()
            raise

    def delete(self, loan_id: int, user_id: int):
        try:
            self.db.query(Loan).filter(
                Loan.id == loan_id and Loan.user_id == user_id).delete()
            self.db.commit()
        except:
            self.db.rollback()
            raise
