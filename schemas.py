from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CompradorBase(BaseModel):
    nome: str

class CompradorCreate(CompradorBase):
    pass

class CompradorSchema(CompradorBase):
    id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    nome: str
    descricao: str
    lance_inicial: float
    data_termino: datetime

class ItemCreate(ItemBase):
    pass

class ItemSchema(ItemBase):
    id: int
    maior_lance: float
    id_maior_lance: Optional[int] = None

    class Config:
        orm_mode = True

class LanceBase(BaseModel):
    valor: float
    id_item: int
    id_comprador: int

class LanceCreate(LanceBase):
    pass

class LanceSchema(LanceBase):
    id: int

    class Config:
        orm_mode = True
