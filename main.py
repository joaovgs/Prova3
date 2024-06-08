from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Buyer, Item, Bid
from schemas import BuyerCreate, ItemCreate, BidCreate, Buyer, Item, Bid
import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/buyers/", response_model=Buyer)
def create_buyer(buyer: BuyerCreate, db: Session = Depends(get_db)):
    return crud.create_buyer(db=db, buyer=buyer)

@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.post("/bids/", response_model=Bid)
def create_bid(bid: BidCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_bid(db=db, bid=bid)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/items/", response_model=list[Item])
def read_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items
