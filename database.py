from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados fornecida pelo Railway
DATABASE_URL = "postgresql://postgres:zPrzbKQnBVvkVHWFzcLEEDHavMdvKWHS@viaduct.proxy.rlwy.net:28886/railway"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()