from sqlalchemy.orm import Session
from app.models.carga import Carga
from app.schemas.carga import CargaOut,CargaCreate
from app.models.carga_item import CargaItem

def get_cargas_by_camion(db:Session, camion_id:int):
    return db.query(Carga).filter(Carga.camion_id==camion_id).all()

def get_carga(db:Session, carga_id:int):
    return db.query(Carga).filter(Carga.id==carga_id).first()


def create_carga(db: Session, carga: CargaCreate, resultados: list[dict]):
    carga_dict = carga.model_dump(exclude={"items"})

    db_carga = Carga(**carga_dict)
    db.add(db_carga)
    db.flush()

    for item in resultados:
        db_item = CargaItem(**item, carga_id=db_carga.id)  # dict directo
        db.add(db_item)

    db.commit()
    db.refresh(db_carga)
    return db_carga

def delete_carga(db:Session, carga_id: int):
    carga = get_carga(db, carga_id)

    if carga:
        db.delete(carga)
        db.commit()
    return carga