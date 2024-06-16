# __init__.py
from .usuarios import Usuario
from .produtos import Produto
from .base import Base

__all__ = ['Base', 'Usuario', 'Produto']