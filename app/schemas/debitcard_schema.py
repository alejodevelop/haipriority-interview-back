from datetime import datetime

from pydantic import BaseModel


class DebitCardCreate(BaseModel):
    card_holder_name: str
    balance: float


class UpdateDebitCard(BaseModel):
    card_holder_name: str


class DebitCardResponse(BaseModel):
    card_number: str
    expiration_date: datetime
    card_holder_name: str
    balance: float
    creation_date: datetime

    class Config:
        from_attributes = True
