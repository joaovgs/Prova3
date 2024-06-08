from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Buyer(Base):
    __tablename__ = "buyers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    start_bid = Column(Float)
    end_time = Column(DateTime)
    highest_bid = Column(Float, default=0.0)
    highest_bidder_id = Column(Integer, ForeignKey('buyers.id'), nullable=True)
    highest_bidder = relationship("Buyer")

class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    item_id = Column(Integer, ForeignKey('items.id'))
    buyer_id = Column(Integer, ForeignKey('buyers.id'))
    item = relationship("Item")
    buyer = relationship("Buyer")
