from typing import Annotated

from fastapi import APIRouter, Depends, status
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from app.services.usuario_service import UserService
from app.utils.auth import get_current_user
from app.utils.logging_config import logger

router = APIRouter()

@router.post("/users/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UsuarioCreate):
    return UserService().create_user(user)

@router.get("/users/", status_code=status.HTTP_201_CREATED)
def get_user(current_user: Annotated[dict , Depends(get_current_user)]):
    logger.info(current_user)
    return "Ejemplo de usuario"