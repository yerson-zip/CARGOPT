from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class CamionCreate(BaseModel):
    placa:str
    largo:float
    ancho:float
    alto:float
    capacidad_kg : float

class CamionOut(BaseModel):
    id: int
    placa:str
    largo : float
    ancho: float
    alto: float
    capacidad_kg: float
    usuario_id:int
    create_on :datetime

    class config:
        from_attributes=True



