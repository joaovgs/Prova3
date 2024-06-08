from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BuyerBase(BaseModel):
    name: str

class BuyerCreate(BuyerBase):
    pass

class Buyer(BuyerBase):
    id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    name: str
    description: str
    start_bid: float
    end_time: datetime

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    highest_bid: float
    highest_bidder_id: Optional[int] = None

    class Config:
        orm_mode = True

class BidBase(BaseModel):
    amount: float
    item_id: int
    buyer_id: int

class BidCreate(BidBase):
    pass

class Bid(BidBase):
    id: int

    class Config:
        orm_mode = True
