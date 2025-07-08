from sqlalchemy.orm       import Session
from app.models.usuarios  import Usuario
from app.schemas.usuarios import UsuarioBase

def read_one(db: Session, usuario: int):
    return db.query(Usuario).filter(Usuario.id == usuario).first()

def read_by_login(db: Session, login: str):
    return db.query(Usuario).filter(Usuario.login == login).first()

def read_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def create(db: Session, usuario: UsuarioBase):
    db_usuario = Usuario(**usuario.model_dump(exclude={"id", "ativo", "dt_criacao", "dt_atualizacao", "ultimo_login"}))
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update(db: Session, id: int, usuario: UsuarioBase):
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if db_usuario is None:
        return None
    for key, value in usuario.model_dump(exclude_unset=True).items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete(db: Session, usuario: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario).first()
    if db_usuario is None:
        return None
    db.delete(db_usuario)
    db.commit()
    return db_usuario
