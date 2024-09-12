from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.cliente_model import Cliente

class ClienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, cliente: Cliente):
        try:
            self.db.add(cliente)
            self.db.commit()
            self.db.refresh(cliente)
            return cliente
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e

    def get_by_documento_identidad(self, documento_identidad: str) -> Cliente:
        return self.db.query(Cliente).filter(Cliente.documento_identidad == documento_identidad).first()
