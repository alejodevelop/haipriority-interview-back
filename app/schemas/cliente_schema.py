from pydantic import BaseModel
from datetime import date

class ClienteCreate(BaseModel):
    nombre: str
    documento_identidad: str
    fecha_nacimiento: date
    direccion: str = None
    telefono: str = None

class ClienteResponse(BaseModel):
    nombre: str
    documento_identidad: str
    fecha_nacimiento: date
    direccion: str = None
    telefono: str = None

    class Config:
        from_attributes = True