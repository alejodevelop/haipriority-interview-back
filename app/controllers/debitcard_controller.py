from typing import Annotated, List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.debitcard_schema import DebitCardCreate, DebitCardResponse, UpdateDebitCard
from app.schemas.token_schema import Payload
from app.services.debitcard_service import DebitCardService
from app.utils.auth import get_current_user

router = APIRouter()


@router.get("/debitcards", response_model=List[DebitCardResponse], status_code=status.HTTP_200_OK)
def get_debitcards(current_user: Annotated[Payload, Depends(get_current_user)], db: Session = Depends(get_db)):
    return DebitCardService(db).get_debitcards(current_user.user_id)


@router.post("/debitcard", response_model=DebitCardResponse, status_code=status.HTTP_201_CREATED)
def create_debitcard(current_user: Annotated[Payload, Depends(get_current_user)], debitcard: DebitCardCreate,
                     db: Session = Depends(get_db)):
    return DebitCardService(db).create_debitcard(debitcard, current_user.user_id)


@router.put("/debitcard/{card_number}", response_model=DebitCardResponse, status_code=status.HTTP_200_OK)
def update_debitcard(current_user: Annotated[Payload, Depends(get_current_user)], card_number,
                     debitcard: UpdateDebitCard,
                     db: Session = Depends(get_db)):
    return DebitCardService(db).update_debitcard_name(card_number, debitcard, current_user.user_id)


@router.put("/debitcard/deposit/{card_number}/{amount}", response_model=DebitCardResponse,
            status_code=status.HTTP_200_OK)
def deposit_debitcard(current_user: Annotated[Payload, Depends(get_current_user)], card_number,
                      amount: float, db: Session = Depends(get_db)):
    return DebitCardService(db).deposit_debitcard(card_number, amount, current_user.user_id)


@router.put("/debitcard/pay/{card_number}/{amount}", response_model=DebitCardResponse, status_code=status.HTTP_200_OK)
def pay_debitcard(current_user: Annotated[Payload, Depends(get_current_user)], card_number,
                  amount: float, db: Session = Depends(get_db)):
    return DebitCardService(db).pay_debitcard(card_number, amount, current_user.user_id)


@router.delete("/debitcard/{card_number}", status_code=status.HTTP_204_NO_CONTENT)
def delete_debitcard(current_user: Annotated[Payload, Depends(get_current_user)], card_number,
                     db: Session = Depends(get_db)):
    return DebitCardService(db).delete_debitcard(card_number, current_user.user_id)
