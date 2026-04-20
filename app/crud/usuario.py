from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.usuario import Usuario
from app.schemas import usuario as she_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_usuario(db:Session, usuario_id:int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def get_usuario_by_email(db:Session, email:str):
    return db.query(Usuario).filter(Usuario.email==email).first()



def create_usuario(db:Session, usuario: she_user.UsuarioCreate):
    hashed = pwd_context.hash(usuario.password)
    db_usuario = Usuario(
        nombre= usuario.nombre,
        email= usuario.email,
        password_hash= hashed
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario