from typing import Annotated, List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.loan_schema import LoanCreate, LoanResponse
from app.schemas.token_schema import Payload
from app.services.loan_service import LoanService
from app.utils.auth import get_current_user

router = APIRouter()


@router.get("/loans", response_model=List[LoanResponse], status_code=status.HTTP_200_OK)
def get_loans(current_user: Annotated[Payload, Depends(get_current_user)], db: Session = Depends(get_db)):
    return LoanService(db).get_loans(current_user.user_id)


@router.post("/loan", response_model=LoanResponse, status_code=status.HTTP_201_CREATED)
def create_loan(current_user: Annotated[Payload, Depends(get_current_user)], loan: LoanCreate,
                db: Session = Depends(get_db)):
    return LoanService(db).create_loan(loan, current_user.user_id)


@router.put("/loan/payoff/{loan_id}/{amount}", response_model=LoanResponse,
            status_code=status.HTTP_200_OK)
def payoff_loan(current_user: Annotated[Payload, Depends(get_current_user)], loan_id,
                amount: float,
                db: Session = Depends(get_db)):
    return LoanService(db).payoff_loan(loan_id, amount, current_user.user_id)


@router.delete("/loan/{loan_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loan(current_user: Annotated[Payload, Depends(get_current_user)], loan_id,
                db: Session = Depends(get_db)):
    return LoanService(db).delete_loan(loan_id, current_user.user_id)
