from sqlalchemy.orm import Session
from .              import models, schemas

def get_indicadores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Indicador).offset(skip).limit(limit).all()

def create_indicador(db: Session, indicador: schemas.IndicadorCreate):
    db_ind = models.Indicador(**indicador.model_dump())
    db.add(db_ind)
    db.commit()
    db.refresh(db_ind)
    return db_ind

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def get_usuario(db: Session, usuario: int):
    db_ind = db.query(models.Usuario).filter(models.Usuario.id == usuario).first()
    if db_ind is None:
        return None
    return db_ind

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_ind = models.Usuario(**usuario.model_dump())
    db.add(db_ind)
    db.commit()
    db.refresh(db_ind)
    return db_ind

def delete_usuario(db: Session, usuario: int):
    db_ind = db.query(models.Usuario).filter(models.Usuario.id == usuario).first()
    if db_ind is None:
        return None
    db.delete(db_ind)
    db.commit()
    return db_ind
