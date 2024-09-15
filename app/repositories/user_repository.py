from sqlalchemy.orm import Session
from app.models.user_model import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except:
            self.db.rollback()
            raise

    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()