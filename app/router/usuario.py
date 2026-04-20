from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import usuario as usuario_DB, camion, carga_item,carga
from app.core.database import get_db, engine
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.crud import usuario

usuario_DB.Base.metadata.create_all(bind=engine)
carga.Base.metadata.create_all(bind=engine)
carga_item.Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/users", tags=["users"])


@router.post("/usuario", response_model=UsuarioOut)
def create_user(user:UsuarioCreate, db:Session=Depends(get_db)):
    request_user = usuario.get_usuario_by_email(db,user.email)
    if request_user:
        raise HTTPException(status_code=400,detail="Email ya registrado")
    return usuario.create_usuario(db,user)


@router.get("/usuario/{usuario_id}", response_model=UsuarioOut)
def obtener_usuario(usuario_id:int, db:Session=Depends(get_db)):
    usuario_db = usuario.get_usuario(db,usuario_id)
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no existente")

    return usuario_db

