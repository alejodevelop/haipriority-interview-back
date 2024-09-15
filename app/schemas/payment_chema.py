from pydantic import BaseModel


class PaymentCreate(BaseModel):
    user_id: int
    amount: float
    product_type: str
    product_id: int


class PaymentResponse(BaseModel):
    id: int
    user_id: int

    class Config:
        from_attributes = True
