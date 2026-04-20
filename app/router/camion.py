from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import camion as CAMION
from app.core.database import get_db, engine
from app.schemas.camion import CamionOut, CamionCreate
from app.crud.usuario import get_usuario
from app.crud import camion as crud


CAMION.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/camiones", tags=["camiones"])


@router.get("/{usuario_id}/camion", response_model=List[CamionOut])
def get_camion_by_userid(usuario_id:int,db:Session=Depends(get_db)):
    return crud.get_camiones_by_usuario(db,usuario_id)

@router.post("/{usuario_id}/camion", response_model=CamionOut)
def creat_camion(usuario_id:int,camion:CamionCreate, db:Session=Depends(get_db)):

    db_usuario = get_usuario(db, usuario_id)


    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no existente")


    return crud.create_camion(db, camion, usuario_id)

@router.delete("/camion_id")
def delete_camion(camion_id:str,  usuario_id:int,db:Session=Depends(get_db)):
    camion = crud.delete_camion(db,camion_id,usuario_id)
    if not camion:
        raise HTTPException(status_code=404, detail="Camión no encontrado")
    return {"mensaje": "Camión eliminado"}