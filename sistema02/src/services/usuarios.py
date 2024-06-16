# src/services/usuarios.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from repository.usuarios import UsuarioRepository
from models.usuarios import Usuario
from schemas.usuarios import Usuario as UsuarioSchema

class UsuarioService:
    def __init__(self, db: Session):
        self.repository = UsuarioRepository(db)

    def get(self, usuario_id):
        usuario = self.repository.get(usuario_id)
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario não encontrado")
        return usuario

    def get_all(self):
        return self.repository.get_all()

    def add(self, usuario : UsuarioSchema):
        usuario = Usuario(**usuario.dict())
        return self.repository.add(usuario)

    def update(self, usuario_id, usuario : UsuarioSchema):
        usuario = Usuario(**usuario.dict())
        return self.repository.update(usuario_id, usuario)

    def delete(self, usuario_id):
        return self.repository.delete(usuario_id)