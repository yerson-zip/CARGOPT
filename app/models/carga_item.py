from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class CargaItem(Base):
    __tablename__ = "carga_items"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    largo  = Column(Float, nullable=False)
    ancho  = Column(Float, nullable=False)
    alto   = Column(Float, nullable=False)
    peso   = Column(Float, nullable=False)
    cantidad = Column(Integer, default=1)
    carga_id = Column(Integer, ForeignKey("cargas.id"), nullable=False)


    pos_x = Column(Float, nullable=True)
    pos_y = Column(Float, nullable=True)
    pos_z = Column(Float, nullable=True)


    carga = relationship("Carga", back_populates="items")