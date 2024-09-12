from sqlalchemy.orm import Session

from app.repositories.cliente_repository import ClienteRepository
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.cliente_schema import ClienteCreate, ClienteResponse
from app.models.cliente_model import Cliente
from fastapi import HTTPException, status

class ClienteService:
    def __init__(self, db: Session):
        self.db = db
        self.cliente_repo = ClienteRepository(self.db)
        self.usuario_repo = UsuarioRepository(self.db)

    def create_cliente(self, cliente: ClienteCreate, email: str) -> ClienteResponse:
        existing_cliente = self.cliente_repo.get_by_documento_identidad(cliente.documento_identidad)
        if existing_cliente:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cliente already registered")

        usuario = self.usuario_repo.get_by_email(email)
        if not usuario:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")

        cliente_data = Cliente(
            nombre=cliente.nombre,
            documento_identidad=cliente.documento_identidad,
            fecha_nacimiento=cliente.fecha_nacimiento,
            direccion=cliente.direccion,
            telefono=cliente.telefono,
            usuario_id=usuario.id
        )

        return self.cliente_repo.create(cliente_data)