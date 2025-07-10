from sqlalchemy.orm import Session
from app.models.metricas import Metrica
from app.schemas.metricas import MetricaBase

def read_one(db: Session, cnes: int, ano: int, mes: int):
    """
    Lê um registro de métrica do banco de dados pela sua chave primária composta.
    """
    return db.query(Metrica).filter(
        Metrica.cnes == cnes,
        Metrica.ano == ano,
        Metrica.mes == mes
    ).first()

def read_all(db: Session, cnes: int, skip: int = 0, limit: int = 100):
    """
    Lê todos os registros de métricas do banco de dados com paginação.
    """
    return db.query(Metrica).filter(Metrica.cnes == cnes).offset(skip).limit(limit).all()

def create(db: Session, metrica: MetricaBase):
    """
    Cria um novo registro de métrica no banco de dados.
    """
    db_metrica = Metrica(**metrica.model_dump())
    db.add(db_metrica)
    db.commit()
    db.refresh(db_metrica)
    return db_metrica

def update(db: Session, cnes: int, ano: int, mes: int, metrica: MetricaBase):
    """
    Atualiza um registro de métrica existente no banco de dados.
    """
    db_metrica = db.query(Metrica).filter(Metrica.cnes==cnes, Metrica.ano==ano, Metrica.mes==mes).first()
    if db_metrica is None:
        return None
    
    update_data = metrica.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_metrica, key, value)
    
    db.commit()
    db.refresh(db_metrica)
    return db_metrica

def delete(db: Session, cnes: int, ano: int, mes: int):
    """
    Deleta um registro de métrica do banco de dados pela sua chave primária composta.
    """
    db_metrica = db.query(Metrica).filter(Metrica.cnes==cnes, Metrica.ano==ano, Metrica.mes==mes).first()
    if db_metrica is None:
        return None
    
    db.delete(db_metrica)
    db.commit()
    return db_metrica