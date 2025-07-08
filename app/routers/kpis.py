from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db
from app.crud import kpis as crud
from app.schemas import kpis as schemas

kpis_router = APIRouter()

@kpis_router.get("/", response_model=List[schemas.Kpi])
def read_kpis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retorna uma lista de KPIs com paginação."""
    kpis = crud.read_all(db, skip=skip, limit=limit)
    return kpis

@kpis_router.get("/{id}", response_model=schemas.Kpi)
def read_kpi(id: int, db: Session = Depends(get_db)):
    """Retorna um KPI específico pelo ID."""
    db_kpi = crud.read_one(db, id)
    if db_kpi is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"KPI com ID {id} não encontrado")
    return db_kpi

@kpis_router.post("/", response_model=schemas.KpiConfirmaAlteracao, status_code=status.HTTP_201_CREATED)
def create_kpi(kpi: schemas.KpiBase, db: Session = Depends(get_db)):
    """Cria um novo KPI caso não exista um KPI com o mesmo título."""
    db_kpi = crud.read_by_titulo(db, kpi.titulo)
    if db_kpi:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="KPI com este título já existe")
    return crud.create(db, kpi)

@kpis_router.put("/{id}", response_model=schemas.KpiConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def update_kpi(id: int, kpi: schemas.KpiBase, db: Session = Depends(get_db)):
    """Atualiza um KPI existente pelo ID."""
    db_kpi = crud.update(db, id, kpi)
    if db_kpi is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"KPI com ID {id} não encontrado")
    return db_kpi

@kpis_router.delete("/{id}", response_model=schemas.KpiConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def delete_kpi(id: int, db: Session = Depends(get_db)):
    """Exclui um KPI existente pelo ID."""
    db_kpi = crud.delete(db, id)
    if db_kpi is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"KPI com ID {id} não encontrado")
    return db_kpi