# src/main.py

from fastapi import FastAPI, Request
from routers import usuarios, produtos
from logging_config import LoggerSetup
import logging

# Cria um logger raiz
logger_setup = LoggerSetup()

# Adiciona o logger para o módulo
LOGGER = logging.getLogger(__name__)

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(produtos.router)

@app.get("/")
async def root(request:Request):
    LOGGER.info("Acessando a rota /")
    return {"message": "Hello World"}
