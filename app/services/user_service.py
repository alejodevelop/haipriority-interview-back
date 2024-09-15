from datetime import datetime

from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from fastapi import HTTPException, status
from app.utils.jwt_config import hash_password, verify_password


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(self.db)

    def create_usuario(self, user: UserCreate):
        existing_user = self.repository.get_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        hashed_password = hash_password(user.password)
        user_data = User(email=user.email, hashed_password=hashed_password, creation_date=datetime.now())
        return self.repository.create(user_data)

    def authenticate_usuario(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user
