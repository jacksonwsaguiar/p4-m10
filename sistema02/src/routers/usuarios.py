# routers/usuarios.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuarios import Usuario as UsuarioSchema
from services.usuarios import UsuarioService
from databases import database
import logging

from rabbitmq.client import RabbitMQClient

rabbitmq_client = RabbitMQClient(host="localhost", queue="logger")

#Cria o logger para o módulo
LOGGER = logging.getLogger(__name__)

router = APIRouter()

@router.get("/usuarios/{usuario_id}")
async def get_usuario(usuario_id: int, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /usuarios/{usuario_id}", "usuario_id": usuario_id, "method": "GET"})
    rabbitmq_client.send_message({"message": "Acessando a rota /usuarios/{usuario_id}", "usuario_id": usuario_id, "method": "GET"})
    usuarioService = UsuarioService(db)
    return usuarioService.get(usuario_id)

@router.get("/usuarios")
async def get_usuarios(db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /usuarios", "method": "GET"})
    rabbitmq_client.send_message({"message": "Acessando a rota /usuarios", "method": "GET"})
    usuarioService = UsuarioService(db)
    return usuarioService.get_all()

@router.post("/usuarios")
async def create_usuario(usuario: UsuarioSchema, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /usuarios", "method": "POST", "usuario": usuario.dict()})
    rabbitmq_client.send_message({"message": "Acessando a rota /usuarios", "method": "POST", "usuario": usuario.dict()})
    usuarioService = UsuarioService(db)
    return usuarioService.add(usuario=usuario)

@router.put("/usuarios/{usuario_id}")
async def update_usuario(usuario_id: int, usuario: UsuarioSchema, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /usuarios/{usuario_id}", "method": "PUT", "usuario_id": usuario_id, "usuario": usuario.dict()})
    rabbitmq_client.send_message({"message": "Acessando a rota /usuarios/{usuario_id}", "method": "PUT", "usuario_id": usuario_id, "usuario": usuario.dict()})
    usuarioService = UsuarioService(db)
    return usuarioService.update(usuario_id, usuario=usuario)
    

@router.delete("/usuarios/{usuario_id}")
async def delete_usuario(usuario_id: int, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /usuarios/{usuario_id}", "method": "DELETE", "usuario_id": usuario_id})
    rabbitmq_client.send_message({"message": "Acessando a rota /usuarios/{usuario_id}", "method": "PUT", "usuario_id": usuario_id, "usuario": usuario.dict()})
    usuarioService = UsuarioService(db)
    return usuarioService.delete(usuario_id)
   