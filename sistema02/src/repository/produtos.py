# src/repository/produtos.py

from models.produtos import Produto
from sqlalchemy.orm import Session
from datetime import datetime

class ProdutoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, produto_id):
        return self.db.query(Produto).get(produto_id)

    def get_all(self):
        return self.db.query(Produto).all()

    def add(self, produto: Produto):
        produto.id = None
        produto.data_criacao = datetime.now()
        self.db.add(produto)
        self.db.flush()
        self.db.commit()
        return {"message": "Produto cadastrado com sucesso"}

    def update(self, produto_id, produto):
        produtodb = self.db.query(Produto).filter(Produto.id == produto_id).first()
        if produtodb is None:
            return {"message": "Produto não encontrado"}
        produto.data_modificacao = datetime.now()
        produto = produto.__dict__
        produto.pop("_sa_instance_state")
        produto.pop("data_criacao")
        produto.pop("id")
        self.db.query(Produto).filter(Produto.id == produto_id).update(produto)
        self.db.flush()
        self.db.commit()
        return {"message": "Produto atualizado com sucesso"}

    def delete(self, produto_id):
        produtodb = self.db.query(Produto).filter(Produto.id == produto_id).first()
        if produtodb is None:
            return {"message": "Produto não encontrado"}
        self.db.query(Produto).filter(Produto.id == produto_id).delete()
        self.db.flush()
        self.db.commit()
        return {"message": "Produto deletado com sucesso"}
        