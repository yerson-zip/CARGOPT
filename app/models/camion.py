from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import  Base

class Camion(Base):

    __tablename__ = "camiones"

    id     = Column(Integer, primary_key=True, index=True)
    placa  = Column(String,nullable=False)
    largo  = Column(Float, nullable=False)
    ancho  = Column(Float, nullable=False)
    alto   = Column(Float, nullable=False)
    capacidad_kg = Column(Float, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    create_on  = Column(DateTime(timezone=True), server_default=func.now())

    usuario = relationship("Usuario", back_populates="camiones")
    cargas  = relationship("Carga", back_populates="camion")
