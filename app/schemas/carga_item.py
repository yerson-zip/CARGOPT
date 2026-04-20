from pydantic import BaseModel
from typing import Optional


class CargaItemCreate(BaseModel):
    nombre: str
    largo: float
    ancho: float
    alto: float
    peso: float
    cantidad: int = 1

class CargaItemOut(BaseModel):
    id: int
    nombre: str
    largo: float
    ancho: float
    alto: float
    peso: float
    cantidad: int
    pos_x: Optional[float]
    pos_y: Optional[float]
    pos_z: Optional[float]

    class Config:
        from_attributes = True