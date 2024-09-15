from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Para desarrollo, se puede cambiar facilmente a PostgreSQL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Importo los modelos para que sqlalchemy los cree en la base de datos
from app.models.user_model import User
from app.models.loan_model import Loan
from app.models.debitcard_model import DebitCard
from app.models.creditcard_model import CreditCard
from app.models.auditlog_model import AuditLog
