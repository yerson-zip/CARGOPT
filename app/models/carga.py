from sqlalchemy import Column, Integer, String,ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Carga(Base):
    __tablename__ = "cargas"

    id     = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    estado      = Column(String,default="pendiente")
    camion_id   = Column(Integer, ForeignKey("camiones.id"), nullable=False)
    creado_en   = Column(DateTime(timezone=True), server_default=func.now())

    camion = relationship("Camion", back_populates="cargas")
    items  = relationship("CargaItem", back_populates="carga", cascade="all, delete-orphan")


