from typing import List

from app.models import carga, carga_item
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db, engine
from app.schemas.carga import CargaCreate, CargaOut
from app.crud import camion as crud_camion
from app.crud import cargas as crud
from app.services import optimizer
carga.Base.metadata.create_all(bind=engine)
carga_item.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/cargas", tags=["cargas"])


@router.get("/camiones/{camion_id}/cargas", response_model=List[CargaOut])
def listar_cargas(camion_id:int,db:Session=Depends(get_db)):

    return crud.get_cargas_by_camion(db,camion_id)

@router.post("/cargas/optimizer")
def crear_carga(carga:CargaCreate, db:Session=Depends(get_db)):
    camion = crud_camion.get_camion_by_id(db, carga.camion_id)

    if not camion:
        raise HTTPException(status_code=404, detail="Camion no existente")

    resultado, no_caben = optimizer.optimizar_carga(camion,carga.items)

    carga = crud.create_carga(db, carga,resultado)

    return {
        "camion": camion,
        "carga":carga,
        "resultado":resultado
    }


@router.get("/{carga_id}/", response_model=CargaOut)
def obtener_carga(carga_id:int, db:Session=Depends(get_db)):
    carga= crud.get_carga(db,carga_id)
    if not carga:
        raise HTTPException(status_code=404, detail="Carga no existente")
    return carga


@router.get("/camiones/{camion_id}/cargas/{carga_id}")
def camion_carga(camion_id: int, carga_id:int,db: Session = Depends(get_db)):
    camion = crud_camion.get_camion_by_id(db,camion_id)


    if not camion:
        raise HTTPException(status_code=404, detail="Camion no existente")

    carga = crud.get_carga(db,carga_id)

    if not carga:
        raise HTTPException(status_code=404, detail="Carga no existente")

    items= carga.items

    carga.items =[]
    if not carga:
        raise HTTPException(status_code=404, detail="Carga no existente")

    return {"camion":camion,
            "carga":carga,
            "items":items
            }
