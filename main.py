from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Buyer, Item, Bid
from schemas import BuyerCreate, ItemCreate, BidCreate, Buyer as BuyerSchema, Item as ItemSchema, Bid as BidSchema
import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/buyers/", response_model=BuyerSchema)
def criar_comprador(buyer: BuyerCreate, db: Session = Depends(get_db)):
    return crud.create_buyer(db=db, buyer=buyer)

@app.post("/items/", response_model=ItemSchema)
def criar_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.post("/bids/", response_model=BidSchema)
def criar_lance(bid: BidCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_bid(db=db, bid=bid)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/items/", response_model=list[ItemSchema])
def listar_itens(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items

@app.get("/buyers/", response_model=list[BuyerSchema])
def listar_compradores(db: Session = Depends(get_db)):
    buyers = crud.get_bidders(db)
    return buyers

@app.get("/bids/", response_model=list[BidSchema])
def listar_lances(db: Session = Depends(get_db)):
    bids = crud.get_bids(db)
    return bids
