from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from config.settings import DB_URL

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)