# src/routers/produtos.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.produtos import Produto as ProdutoSchema
from services.produtos import ProdutoService
from databases import database
import logging

from rabbitmq.client import RabbitMQClient

rabbitmq_client = RabbitMQClient(host="localhost", queue="logger")

LOGGER = logging.getLogger(__name__)

router = APIRouter()

@router.get("/produtos/{produto_id}")
async def get_produto(produto_id: int, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /produtos/{produto_id}", "produto_id": produto_id, "method": "GET"})
    rabbitmq_client.send_message({"message": "Acessando a rota /produtos/{produto_id}", "produto_id": produto_id, "method": "GET"})
    produtoService = ProdutoService(db)
    return produtoService.get(produto_id)

@router.get("/produtos")
async def get_produtos(db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /produtos", "method": "GET"})
    rabbitmq_client.send_message({"message": "Acessando a rota /produtos", "method": "GET"})
    produtoService = ProdutoService(db)
    return produtoService.get_all()

@router.post("/produtos")
async def create_produto(produto: ProdutoSchema, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /produtos", "method": "POST", "produto": produto.dict()})
    rabbitmq_client.send_message({"message": "Acessando a rota /produtos", "method": "POST", "produto": produto.dict()})
    produtoService = ProdutoService(db)
    return produtoService.add(produto=produto)

@router.put("/produtos/{produto_id}")
async def update_produto(produto_id: int, produto: ProdutoSchema, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /produtos/{produto_id}", "method": "PUT", "produto_id": produto_id, "produto": produto.dict()})
    rabbitmq_client.send_message({"message": "Acessando a rota /produtos/{produto_id}", "method": "PUT", "produto_id": produto_id, "produto": produto.dict()})
    produtoService = ProdutoService(db)
    return produtoService.update(produto_id, produto=produto)
    

@router.delete("/produtos/{produto_id}")
async def delete_produto(produto_id: int, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /produtos/{produto_id}", "method": "DELETE", "produto_id": produto_id})
    rabbitmq_client.send_message({"message": "Acessando a rota /produtos/{produto_id}", "method": "DELETE", "produto_id": produto_id})
    produtoService = ProdutoService(db)
    return produtoService.delete(produto_id)