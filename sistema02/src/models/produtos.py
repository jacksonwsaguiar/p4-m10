# produtos.py
from sqlalchemy import Column, Integer, String, Double, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Double)
    data_criacao = Column(DateTime)
    data_modificacao = Column(DateTime)

    def __repr__(self):
        return f"<Produto(nome='{self.nome}', descricao='{self.descricao}, id={self.id}', criado_em='{self.data_criacao}', modificado_em='{self.data_modificacao}')>"