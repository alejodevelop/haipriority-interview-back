from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: Usuario):
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except:
            self.db.rollback()
            raise

    def get_by_email(self, email: str) -> Usuario:
        return self.db.query(Usuario).filter(Usuario.email == email).first()