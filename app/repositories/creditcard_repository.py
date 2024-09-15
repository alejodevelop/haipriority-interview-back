from typing import List

from sqlalchemy import inspect
from sqlalchemy.orm import Session
from app.models.creditcard_model import CreditCard


class CreditCardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, creditCard: CreditCard):
        try:
            self.db.add(creditCard)
            self.db.commit()
            self.db.refresh(creditCard)
            return creditCard
        except:
            self.db.rollback()
            raise

    def get_by_card_number(self, card_number: str) -> CreditCard:
        return self.db.query(CreditCard).filter(CreditCard.card_number == card_number).first()

    def get_by_user_id(self, user_id: int) -> List[CreditCard]:
        return self.db.query(CreditCard).filter(CreditCard.user_id == user_id).all()

    def update(self, card_number: str, creditcard: CreditCard, user_id: int):
        try:
            # Obtener las columnas del modelo CreditCard
            creditcard_columns = {c.key for c in inspect(CreditCard).mapper.column_attrs}

            # Convertimos el objeto CreditCard en un diccionario, ignorando los que no sean columnas
            update_data = {key: value for key, value in creditcard.__dict__.items() if
                           key in creditcard_columns and value is not None}

            # Actualizamos solo los campos que no sean None y que existan como columnas en el modelo
            self.db.query(CreditCard).filter(
                CreditCard.card_number == card_number and CreditCard.user_id == user_id).update(update_data)
            self.db.commit()
            return creditcard
        except:
            self.db.rollback()
            raise

    def delete(self, card_number: str, user_id: int):
        try:
            self.db.query(CreditCard).filter(
                CreditCard.card_number == card_number and CreditCard.user_id == user_id).delete()
            self.db.commit()
        except:
            self.db.rollback()
            raise
