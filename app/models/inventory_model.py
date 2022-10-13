from sqlalchemy import Column,Integer,Float,Date
from app.db.postgres.pg_core import Base
from sqlalchemy.orm import relationship

class InventoryModel(Base):
    FechaInventario = Column(Date)
    GLN_Cliente = Column(Integer)
    GLN_sucursal = Column(Integer)
    Gtin_Producto = Column(Integer)
    Inventario_Final = Column(Integer)
    PrecioUnidad = Column(Float)