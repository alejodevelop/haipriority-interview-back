from sqlalchemy.orm import Session

from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario_schema import UsuarioCreate
from app.models.usuario_model import Usuario
from fastapi import HTTPException, status
from app.utils.jwt_config import hash_password, verify_password


class UsuarioService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = UsuarioRepository(self.db)

    def create_usuario(self, user: UsuarioCreate):
        existing_user = self.repository.get_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        hashed_password = hash_password(user.password)
        user_data = Usuario(email=user.email, hashed_password=hashed_password)
        return self.repository.create(user_data)

    def authenticate_usuario(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user
