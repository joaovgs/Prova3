from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Comprador, Item, Lance
from schemas import CompradorCreate, ItemCreate, LanceCreate, CompradorSchema, ItemSchema, LanceSchema
import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/compradores/", response_model=CompradorSchema)
def criar_comprador(comprador: CompradorCreate, db: Session = Depends(get_db)):
    return crud.criar_comprador(db=db, comprador=comprador)

@app.get("/compradores/", response_model=list[CompradorSchema])
def listar_compradores(db: Session = Depends(get_db)):
    return crud.pegar_compradores(db)

@app.post("/itens/", response_model=ItemSchema)
def criar_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.criar_item(db=db, item=item)

@app.get("/itens/", response_model=list[ItemSchema])
def listar_itens(db: Session = Depends(get_db)):
    return crud.pegar_itens(db)

@app.post("/lances/", response_model=LanceSchema)
def criar_lance(lance: LanceCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar_lance(db=db, lance=lance)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/lances/", response_model=list[LanceSchema])
def listar_lances(db: Session = Depends(get_db)):
    return crud.pegar_lances(db)
