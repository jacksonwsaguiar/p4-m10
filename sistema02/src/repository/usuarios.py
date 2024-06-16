# src/repository/usuarios.py

from models.usuarios import Usuario
from sqlalchemy.orm import Session
from datetime import datetime

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, usuario_id):
        return self.db.query(Usuario).get(usuario_id)

    def get_all(self):
        return self.db.query(Usuario).all()

    def add(self, usuario: Usuario):
        usuario.id = None
        usuario.data_criacao = datetime.now()
        self.db.add(usuario)
        self.db.flush()
        self.db.commit()
        return {"message": "Usuário cadastrado com sucesso"}

    def update(self, usuario_id, usuario):
        usuariodb = self.db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if usuariodb is None:
            return {"message": "Usuário não encontrado"}
        usuario.data_modificacao = datetime.now()
        usuario = usuario.__dict__
        usuario.pop("_sa_instance_state")
        usuario.pop("data_criacao")
        usuario.pop("id")
        self.db.query(Usuario).filter(Usuario.id == usuario_id).update(usuario)
        self.db.flush()
        self.db.commit()
        return {"message": "Usuário atualizado com sucesso"}

    def delete(self, usuario_id):
        usuariodb = self.db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if usuariodb is None:
            return {"message": "Usuário não encontrado"}
        self.db.query(Usuario).filter(Usuario.id == usuario_id).delete()
        self.db.flush()
        self.db.commit()
        return {"message": "Usuário deletado com sucesso"}
        