from sqlalchemy.orm       import Session
from app.models.empresas  import Empresa
from app.schemas.empresas import EmpresaBase

def read_one(db: Session, empresa: int):
    return db.query(Empresa).filter(Empresa.id == empresa).first()

def read_by_cnpj_cnes(db: Session, cnpj: str, cnes: int):
    return db.query(Empresa).filter(Empresa.cnpj == cnpj, Empresa.cnes == cnes).first()

def read_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Empresa).offset(skip).limit(limit).all()

def create(db: Session, empresa: EmpresaBase):
    db_empresa = Empresa(**empresa.model_dump(exclude={"id", "ativo", "dt_criacao", "dt_atualizacao", "ultimo_login"}))
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def update(db: Session, id: int, empresa: EmpresaBase):
    db_empresa = db.query(Empresa).filter(Empresa.id == id).first()
    if db_empresa is None:
        return None
    for key, value in empresa.model_dump(exclude_unset=True).items():
        setattr(db_empresa, key, value)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def delete(db: Session, empresa: int):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa).first()
    if db_empresa is None:
        return None
    db.delete(db_empresa)
    db.commit()
    return db_empresa
