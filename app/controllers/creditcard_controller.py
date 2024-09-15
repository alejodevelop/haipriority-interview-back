from typing import Annotated, List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.creditcard_schema import CreditCardCreate, CreditCardResponse, CreditCardUpdate
from app.schemas.token_schema import Payload
from app.services.creditcard_service import CreditCardService
from app.utils.auth import get_current_user

router = APIRouter()


@router.get("/creditcards", response_model=List[CreditCardResponse], status_code=status.HTTP_200_OK)
def get_creditcards(current_user: Annotated[Payload, Depends(get_current_user)], db: Session = Depends(get_db)):
    return CreditCardService(db).get_creditcards(current_user.user_id)


@router.post("/creditcard", response_model=CreditCardResponse, status_code=status.HTTP_201_CREATED)
def create_creditcard(current_user: Annotated[Payload, Depends(get_current_user)], creditcard: CreditCardCreate,
                      db: Session = Depends(get_db)):
    return CreditCardService(db).create_creditcard(creditcard, current_user.user_id)


@router.put("/creditcard/{card_number}", response_model=CreditCardResponse, status_code=status.HTTP_200_OK)
def update_creditcard(current_user: Annotated[Payload, Depends(get_current_user)], card_number,
                      creditcard: CreditCardUpdate,
                      db: Session = Depends(get_db)):
    return CreditCardService(db).update_creditcard_name(card_number, creditcard, current_user.user_id)


@router.put("/creditcard/pay/{card_number}/{amount}", response_model=CreditCardResponse,
            status_code=status.HTTP_200_OK)
def pay_creditcard(current_user: Annotated[Payload, Depends(get_current_user)], card_number,
                   amount: float,
                   db: Session = Depends(get_db)):
    return CreditCardService(db).pay_creditcard(card_number, amount, current_user.user_id)


@router.put("/creditcard/payoff/{card_number}/{amount}", response_model=CreditCardResponse,
            status_code=status.HTTP_200_OK)
def payoff_creditcard(current_user: Annotated[Payload, Depends(get_current_user)], card_number,
                      amount: float,
                      db: Session = Depends(get_db)):
    return CreditCardService(db).payoff_creditcard(card_number, amount, current_user.user_id)


@router.delete("/creditcard/{card_number}", status_code=status.HTTP_204_NO_CONTENT)
def delete_creditcard(current_user: Annotated[Payload, Depends(get_current_user)], card_number,
                      db: Session = Depends(get_db)):
    return CreditCardService(db).delete_creditcard(card_number, current_user.user_id)
