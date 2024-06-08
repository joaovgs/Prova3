from sqlalchemy.orm import Session
from models import Buyer, Item, Bid
from schemas import BuyerCreate, ItemCreate, BidCreate
from datetime import datetime

def get_buyer(db: Session, buyer_id: int):
    return db.query(Buyer).filter(Buyer.id == buyer_id).first()

def create_buyer(db: Session, buyer: BuyerCreate):
    db_buyer = Buyer(name=buyer.name)
    db.add(db_buyer)
    db.commit()
    db.refresh(db_buyer)
    return db_buyer

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_bid(db: Session, bid: BidCreate):
    db_item = get_item(db, bid.item_id)
    if db_item.end_time < datetime.now():
        raise Exception("Auction has ended.")
    if bid.amount <= db_item.highest_bid:
        raise Exception("Bid must be higher than the current highest bid.")
    db_bid = Bid(amount=bid.amount, item_id=bid.item_id, buyer_id=bid.buyer_id)
    db_item.highest_bid = bid.amount
    db_item.highest_bidder_id = bid.buyer_id
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid

def get_items(db: Session):
    return db.query(Item).all()
