from sqlalchemy import Column, Integer, String
from app.database import Base


class Usuario(Base):
    __tablename__ = 'Usuario'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
