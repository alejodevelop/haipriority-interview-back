from datetime import datetime

from dateutil.relativedelta import relativedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.models.debitcard_model import DebitCard
from app.repositories.debitcard_repository import DebitCardRepository
from app.schemas.debitcard_schema import DebitCardCreate, UpdateDebitCard
from app.utils.card_number_generator import generate_card_number

EXPIRATION_DATE = 3
DEBITCARD_NOT_FOUND = "Debit card not found"


class DebitCardService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = DebitCardRepository(self.db)

    def create_debitcard(self, debitcard: DebitCardCreate, user_id: int):
        card_number = generate_card_number()
        card_number_exists = self.repository.get_by_card_number(card_number)
        while card_number_exists:
            card_number = generate_card_number()
            card_number_exists = self.repository.get_by_card_number(card_number)

        debit_card = DebitCard(
            user_id=user_id,
            card_number=card_number,
            expiration_date=datetime.now() + relativedelta(years=EXPIRATION_DATE),
            card_holder_name=debitcard.card_holder_name,
            balance=debitcard.balance,
            creation_date=datetime.now(),
        )
        return self.repository.create(debit_card)

    def get_debitcards(self, user_id: int):
        return self.repository.get_by_user_id(user_id)

    def update_debitcard_name(self, card_number: str, debitcard: UpdateDebitCard, user_id: int):
        existing_debitcard = self.repository.get_by_card_number(card_number)
        if not existing_debitcard:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=DEBITCARD_NOT_FOUND)

        existing_debitcard.card_holder_name = debitcard.card_holder_name

        return self.repository.update(card_number, existing_debitcard, user_id)

    def deposit_debitcard(self, card_number: str, amount: float, user_id: int):
        existing_debitcard = self.repository.get_by_card_number(card_number)
        if not existing_debitcard:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=DEBITCARD_NOT_FOUND)

        existing_debitcard.balance += amount

        return self.repository.update(card_number, existing_debitcard, user_id)

    def pay_debitcard(self, card_number: str, amount: float, user_id: int):
        existing_debitcard = self.repository.get_by_card_number(card_number)
        if not existing_debitcard:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=DEBITCARD_NOT_FOUND)

        if existing_debitcard.balance < amount:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient balance")

        existing_debitcard.balance -= amount

        return self.repository.update(card_number, existing_debitcard, user_id)

    def delete_debitcard(self, card_number: str, user_id: int):
        existing_debitcard = self.repository.get_by_card_number(card_number)
        if not existing_debitcard:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=DEBITCARD_NOT_FOUND)

        return self.repository.delete(card_number, user_id)
