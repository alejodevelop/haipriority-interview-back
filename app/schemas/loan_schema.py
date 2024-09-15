from datetime import datetime

from pydantic import BaseModel


class LoanCreate(BaseModel):
    amount: float


class LoanResponse(BaseModel):
    id: int
    amount: float
    interest_rate: float
    balance: float
    start_date: datetime
    end_date: datetime
    creation_date: datetime

    class Config:
        from_attributes = True
