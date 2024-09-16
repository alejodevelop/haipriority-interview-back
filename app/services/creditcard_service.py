from datetime import datetime

from dateutil.relativedelta import relativedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.models.creditcard_model import CreditCard
from app.repositories.creditcard_repository import CreditCardRepository
from app.schemas.creditcard_schema import CreditCardCreate, CreditCardUpdate
from app.utils.card_number_generator import generate_card_number
from app.utils.credit_limit_calculator import calculate_credit_limit

EXPIRATION_DATE = 2
CREDITCARD_NOT_FOUND = "Credit card not found"


class CreditCardService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = CreditCardRepository(self.db)

    def create_creditcard(self, creditcard: CreditCardCreate, user_id: int):
        card_number = generate_card_number()
        card_number_exists = self.repository.get_by_card_number(card_number)
        while card_number_exists:
            card_number = generate_card_number()
            card_number_exists = self.repository.get_by_card_number(card_number)

        credit_limit = calculate_credit_limit(user_id)  # AI FEATURE

        if 0 >= credit_limit:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Our AI system has determined that you are not eligible to receive a credit card")

        debit_card = CreditCard(
            user_id=user_id,
            card_number=card_number,
            expiration_date=datetime.now() + relativedelta(years=EXPIRATION_DATE),
            card_holder_name=creditcard.card_holder_name,
            credit_limit=credit_limit,
            balance=0,
            creation_date=datetime.now(),
        )
        return self.repository.create(debit_card)

    def get_creditcards(self, user_id: int):
        return self.repository.get_by_user_id(user_id)

    def update_creditcard_name(self, card_number: str, creditcard: CreditCardUpdate, user_id: int):
        existing_creditcard = self.repository.get_by_card_number(card_number)
        if not existing_creditcard:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=CREDITCARD_NOT_FOUND)

        existing_creditcard.card_holder_name = creditcard.card_holder_name

        return self.repository.update(card_number, existing_creditcard, user_id)

    def pay_creditcard(self, card_number: str, amount: float, user_id: int):
        existing_creditcard = self.repository.get_by_card_number(card_number)
        if not existing_creditcard:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=CREDITCARD_NOT_FOUND)

        if existing_creditcard.credit_limit < existing_creditcard.balance + amount:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient funds, credit limit exceeded")

        existing_creditcard.balance += amount

        return self.repository.update(card_number, existing_creditcard, user_id)

    def payoff_creditcard(self, card_number: str, amount: float, user_id: int):
        existing_creditcard = self.repository.get_by_card_number(card_number)
        if not existing_creditcard:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=CREDITCARD_NOT_FOUND)

        if 0 > existing_creditcard.balance - amount:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="you can't pay more than the total debt")

        existing_creditcard.balance -= amount

        return self.repository.update(card_number, existing_creditcard, user_id)

    def delete_creditcard(self, card_number: str, user_id: int):
        existing_creditcard = self.repository.get_by_card_number(card_number)
        if not existing_creditcard:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=CREDITCARD_NOT_FOUND)

        return self.repository.delete(card_number, user_id)
