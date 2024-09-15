from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class Payload(BaseModel):
    email: str
    user_id: int
