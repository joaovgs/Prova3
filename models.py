from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Comprador(Base):
    __tablename__ = "compradores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

class Item(Base):
    __tablename__ = "itens"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String, index=True)
    lance_inicial = Column(Float)
    tempo_final = Column(DateTime)
    maior_lance = Column(Float, default=0.0)
    id_maior_lance = Column(Integer, ForeignKey('compradores.id'), nullable=True)
    maior_lance_comprador = relationship("Comprador")

class Lance(Base):
    __tablename__ = "lances"
    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float)
    id_item = Column(Integer, ForeignKey('itens.id'))
    id_comprador = Column(Integer, ForeignKey('compradores.id'))
    item = relationship("Item")
    comprador = relationship("Comprador")
