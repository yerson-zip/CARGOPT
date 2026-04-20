from pydantic import BaseModel, EmailStr
from datetime import datetime


class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str


class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: str
    activo: bool
    creat_on: datetime

    class Config:
        from_attributes = True