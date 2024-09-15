from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class AuditAction(enum.Enum):
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'


class AuditLog(Base):
    __tablename__ = 'audit_logs'

    id = Column(Integer, primary_key=True, index=True)
    table_name = Column(String, nullable=False)
    record_id = Column(Integer, nullable=False)
    old_values = Column(String)  # JSON or text field to store old values
    new_values = Column(String)  # JSON or text field to store new values
    action = Column(Enum(AuditAction), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))  # Who made the change
    timestamp = Column(DateTime, default=func.now(), nullable=False)

    user = relationship("User", back_populates="audit_logs")
