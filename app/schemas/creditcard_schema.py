from datetime import datetime

from pydantic import BaseModel


class CreditCardCreate(BaseModel):
    card_holder_name: str


class CreditCardUpdate(BaseModel):
    card_holder_name: str


class CreditCardResponse(BaseModel):
    card_number: str
    expiration_date: datetime
    card_holder_name: str
    credit_limit: float
    balance: float
    creation_date: datetime

    class Config:
        from_attributes = True
