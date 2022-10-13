from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base

from app.settings.settings import settings
from typing import Any

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

# @as_declarative()
# class Base:
#     id: Any
#     __name__: str
    
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__tablename__.lower()