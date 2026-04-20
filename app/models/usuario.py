from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import  Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id      = Column(Integer, primary_key=True, index=True)
    nombre  = Column(String, nullable=False)
    email   = Column(String, unique=True, index=True,nullable=False)
    password_hash = Column(String, nullable=False)
    activo  = Column(Boolean, default=True)
    creat_on= Column(DateTime(timezone=True), server_default=func.now())

    camiones = relationship("Camion", back_populates="usuario")

