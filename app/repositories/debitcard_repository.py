from typing import List

from sqlalchemy import inspect
from sqlalchemy.orm import Session
from app.models.debitcard_model import DebitCard


class DebitCardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, debitcard: DebitCard):
        try:
            self.db.add(debitcard)
            self.db.commit()
            self.db.refresh(debitcard)
            return debitcard
        except:
            self.db.rollback()
            raise

    def get_by_card_number(self, card_number: str) -> DebitCard:
        return self.db.query(DebitCard).filter(DebitCard.card_number == card_number).first()

    def get_by_user_id(self, user_id: int) -> List[DebitCard]:
        return self.db.query(DebitCard).filter(DebitCard.user_id == user_id).all()

    def update(self, card_number: str, debitcard: DebitCard, user_id: int):
        try:
            # Obtener las columnas del modelo DebitCard
            debitcard_columns = {c.key for c in inspect(DebitCard).mapper.column_attrs}

            # Convertimos el objeto DebitCardCreate en un diccionario, ignorando los que no sean columnas
            update_data = {key: value for key, value in debitcard.__dict__.items() if
                           key in debitcard_columns and value is not None}

            # Actualizamos solo los campos que no sean None y que existan como columnas en el modelo
            self.db.query(DebitCard).filter(
                DebitCard.card_number == card_number and DebitCard.user_id == user_id).update(update_data)
            self.db.commit()
            return debitcard
        except:
            self.db.rollback()
            raise

    def delete(self, card_number: str, user_id: int):
        try:
            self.db.query(DebitCard).filter(
                DebitCard.card_number == card_number and DebitCard.user_id == user_id).delete()
            self.db.commit()
        except:
            self.db.rollback()
            raise
