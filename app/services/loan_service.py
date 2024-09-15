from datetime import datetime

from dateutil.relativedelta import relativedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.models.loan_model import Loan
from app.repositories.loan_repository import LoanRepository
from app.schemas.loan_schema import LoanCreate
from app.utils.credit_limit_calculator import calculate_credit_limit
from app.utils.interest_rate_calculator import interest_rate_calculator

EXPIRATION_DATE = 1
LOAN_NOT_FOUND = "Loan not found"


class LoanService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = LoanRepository(self.db)

    def create_loan(self, loan: LoanCreate, user_id: int):

        credit_limit = calculate_credit_limit(user_id)  # AI FEATURE
        interest_rate = interest_rate_calculator(user_id, loan.amount)  # AI FEATURE

        if loan.amount > credit_limit:
            raise ValueError("Our AI system has determined that you are not eligible to borrow this amount")

        if loan.amount <= 0:
            raise ValueError("you can't borrow 0 or less")

        debit_card = Loan(
            user_id=user_id,
            amount=loan.amount,
            interest_rate=interest_rate,  # decimal format of interest rate
            start_date=datetime.now(),
            end_date=datetime.now() + relativedelta(years=EXPIRATION_DATE),
            balance=loan.amount * (1 + interest_rate),
            creation_date=datetime.now(),
        )
        return self.repository.create(debit_card)

    def get_loans(self, user_id: int):
        return self.repository.get_by_user_id(user_id)

    def payoff_loan(self, loan_id: int, amount: float, user_id: int):
        existing_loan = self.repository.get_by_loan_id(loan_id)
        if not existing_loan:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=LOAN_NOT_FOUND)

        if 0 > existing_loan.balance - amount:
            raise ValueError("you can't pay more than the total debt")

        existing_loan.balance -= amount

        return self.repository.update(loan_id, existing_loan, user_id)

    def delete_loan(self, loan_id: int, user_id: int):
        existing_loan = self.repository.get_by_loan_id(loan_id)
        if not existing_loan:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=LOAN_NOT_FOUND)

        return self.repository.delete(loan_id, user_id)
