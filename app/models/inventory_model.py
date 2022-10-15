from sqlalchemy import Column,Integer,Float,Date,String,Text,BigInteger
from app.db.postgres.pg_core import Base
from sqlalchemy.orm import relationship

class ClienteModel(Base):
    id = Column(BigInteger, primary_key=True,index=True)
    cliente = relationship("InventoryModel", back_populates="GLN_Cliente")

class ClienteModel(Base):
    id = Column(BigInteger, primary_key=True,index=True)
    surcursal = relationship("InventoryModel", back_populates="GLN_sucursal")

class ClienteModel(Base):
    id = Column(BigInteger, primary_key=True,index=True)
    producto = relationship("InventoryModel", back_populates="Gtin_Producto")


class InventoryModel(Base):
    __tablename__ = "inventory"
    id = Column(BigInteger, primary_key=True,index=True)
    FechaInventario = Column(Text)
    GLN_Cliente = Column(String)
    GLN_sucursal = Column(String)
    Gtin_Producto = Column(String)
    Inventario_Final = Column(String)
    PrecioUnidad = Column(Float)