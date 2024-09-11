from app.repositories.usuario_repository import UserRepository
from app.schemas.usuario_schema import UsuarioCreate
from app.models.usuario_model import Usuario
from fastapi import HTTPException, status
from app.database import get_db
from app.utils.utils import hash_password, verify_password

class UserService:
    def __init__(self):
        self.db = next(get_db())
        self.repository = UserRepository(self.db)

    def create_user(self, user: UsuarioCreate):
        try:
            existing_user = self.repository.get_by_email(user.email)
            if existing_user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

            hashed_password = hash_password(user.password)
            user_data = Usuario(email=user.email, hashed_password=hashed_password)
            return self.repository.create(user_data)
        finally:
            self.db.close()

    def authenticate_user(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user
