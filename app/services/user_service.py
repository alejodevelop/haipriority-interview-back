from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from app.models.user_model import User
from fastapi import HTTPException, status
from app.database import get_db
from app.utils.utils import hash_password

class UserService:
    def __init__(self):
        self.db = next(get_db())
        self.repository = UserRepository(self.db)

    def create_user(self, user: UserCreate):
        try:
            existing_user = self.repository.get_by_email(user.email)
            if existing_user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

            hashed_password = hash_password(user.password)
            user_data = User(name=user.name, email=user.email, hashed_password=hashed_password)
            return self.repository.create(user_data)
        finally:
            self.db.close()