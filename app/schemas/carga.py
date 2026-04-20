from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.carga_item import CargaItemCreate, CargaItemOut


class CargaCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    camion_id: int
    items: List[CargaItemCreate] = []

class CargaOut(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str]
    estado: str
    camion_id: int
    creado_en: datetime
    """
    Debo cambiar esta linea a 
    items : List[CargaItemOut]
    cuando se implemente py3dbp
    """
    items: List[CargaItemOut] = []

    class Config:
        from_attributes = True
