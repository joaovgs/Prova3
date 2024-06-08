from sqlalchemy.orm import Session
from models import Comprador, Item, Lance
from schemas import CompradorCreate, ItemCreate, LanceCreate
from datetime import datetime

def get_comprador(db: Session, comprador_id: int):
    return db.query(Comprador).filter(Comprador.id == comprador_id).first()

def criar_comprador(db: Session, comprador: CompradorCreate):
    db_comprador = Comprador(nome=comprador.nome)
    db.add(db_comprador)
    db.commit()
    db.refresh(db_comprador)
    return db_comprador

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def criar_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def criar_lance(db: Session, lance: LanceCreate):
    db_item = get_item(db, lance.id_item)
    if db_item.tempo_final < datetime.now():
        raise Exception("O leilão já terminou.")
    if lance.valor <= db_item.maior_lance:
        raise Exception("O lance deve ser maior que o lance atual.")
    db_lance = Lance(valor=lance.valor, id_item=lance.id_item, id_comprador=lance.id_comprador)
    db_item.maior_lance = lance.valor
    db_item.id_maior_lance = lance.id_comprador
    db.add(db_lance)
    db.commit()
    db.refresh(db_lance)
    return db_lance

def pegar_itens(db: Session):
    return db.query(Item).all()
