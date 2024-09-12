from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    documento_identidad = Column(String, unique=True, index=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

    usuario = relationship("Usuario", back_populates="cliente")