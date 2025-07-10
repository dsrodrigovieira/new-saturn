from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db
from app.crud import metricas as crud
from app.schemas import metricas as schemas

metricas_router = APIRouter()

@metricas_router.get("/{cnes}", response_model=List[schemas.Metrica])
def read_metricas(cnes: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retorna uma lista de métricas de competências com paginação."""
    db_metricas = crud.read_all(db, cnes=cnes, skip=skip, limit=limit)
    if db_metricas is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foram encontradas métricas para o CNES {cnes}.")
    return db_metricas

@metricas_router.get("/{cnes}/{ano}/{mes}", response_model=schemas.Metrica)
def read_metrica(cnes: int, ano: int, mes: int, db: Session = Depends(get_db)):
    """Retorna as métricas de uma competência específica."""
    db_metricas = crud.read_one(db, cnes=cnes, ano=ano, mes=mes)
    if db_metricas is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foram encontradas métricas para o CNES {cnes} na competência de {mes}/{ano}.")
    return db_metricas

@metricas_router.post("/", response_model=schemas.MetricaConfirmaAlteracao, status_code=status.HTTP_201_CREATED)
def create_metrica(metrica: schemas.Metrica, db: Session = Depends(get_db)):
    """Cria as métricas de uma nova competência caso não exista."""
    cnes = metrica.cnes
    ano = metrica.ano
    mes = metrica.mes
    db_metrica = crud.read_one(db, cnes=cnes, ano=ano, mes=mes)
    if db_metrica:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existem métricas para o CNES {cnes} na competência de {mes}/{ano}.")
    return crud.create(db, metrica)

@metricas_router.put("/{cnes}/{ano}/{mes}", response_model=schemas.MetricaConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def update_metrica(cnes: int, ano: int, mes: int, metrica: schemas.MetricaBase, db: Session = Depends(get_db)):
    """Atualiza as métricas de uma competência existente."""
    db_metrica = crud.update(db, cnes=cnes, ano=ano, mes=mes, metrica=metrica)
    if db_metrica is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foram encontradas métricas para o CNES {cnes} na competência de {mes}/{ano}.")
    return db_metrica

@metricas_router.delete("/{cnes}/{ano}/{mes}", response_model=schemas.MetricaConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def delete_metrica(cnes: int, ano: int, mes: int, db: Session = Depends(get_db)):
    """Exclui as métircas de uma competência existente pelo."""
    db_metrica = crud.delete(db, cnes=cnes, ano=ano, mes=mes)
    if db_metrica is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foram encontradas métricas para o CNES {cnes} na competência de {mes}/{ano}.")
    return db_metrica