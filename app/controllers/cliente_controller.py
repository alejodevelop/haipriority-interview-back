from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.cliente_schema import ClienteResponse, ClienteCreate
from app.schemas.token_schema import Payload
from app.services.cliente_service import ClienteService
from app.utils.auth import get_current_user

router = APIRouter()


@router.post("/cliente", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def create_cliente(cliente: ClienteCreate, current_user: Annotated[Payload, Depends(get_current_user)], db: Session = Depends(get_db)):
    return ClienteService(db).create_cliente(cliente, current_user.email)
