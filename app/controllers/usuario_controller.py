from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from app.services.usuario_service import UsuarioService
from app.utils.auth import get_current_user
from app.utils.logging_config import logger

router = APIRouter()


@router.post("/usuario", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def create_usuario(user: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioService(db).create_usuario(user)


@router.get("/usuarios", status_code=status.HTTP_201_CREATED)
def get_usuarios(current_user: Annotated[dict, Depends(get_current_user)]):
    logger.info(current_user)
    return "Ejemplo de usuario"
