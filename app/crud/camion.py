from sqlalchemy.orm import Session
from app.models.camion import Camion
from app.schemas.camion import CamionOut, CamionCreate

def get_camiones_by_usuario(db:Session, usuario_id:int):
    return db.query(Camion).filter(Camion.usuario_id==usuario_id).all()

def get_camion_by_id(db:Session, camion_id:int):
    return db.query(Camion).filter(Camion.id==camion_id).first()

def create_camion(db:Session, camion: CamionCreate, usuario_id:int):
    db_camion = Camion(**camion.model_dump(), usuario_id=usuario_id)

    db.add(db_camion)
    db.commit()
    db.refresh(db_camion)
    return db_camion


def delete_camion(db:Session, camion_id:int, usuario_id:int):
    camion = db.query(Camion).filter(
        Camion.id == camion_id,
        Camion.usuario_id == usuario_id
    ).first()

    if camion:
        db.delete(camion)
        db.commit()

    return camion