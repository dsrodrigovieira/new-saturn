from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import empresas as schemas
from app.crud import empresas as crud
from app.dependencies import get_db
from typing import List

empresas_router = APIRouter()

@empresas_router.get("/", response_model=List[schemas.EmpresaBase])
def read_empresas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retorna uma lista de empresas com paginação."""
    return crud.read_all(db, skip=skip, limit=limit)

@empresas_router.get("/{id}", response_model=schemas.EmpresaBase)
def read_empresa(id: int, db: Session = Depends(get_db)):
    """Retorna uma empresa específica pelo ID."""
    empresa = crud.read_one(db, id)
    if empresa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Empresa com ID {id} não encontrada")
    return empresa

@empresas_router.post("/", response_model=schemas.EmpresaConfirmaAlteracao, status_code=status.HTTP_201_CREATED)
def create_empresa(emp: schemas.EmpresaBase, db: Session = Depends(get_db)):
    """Cria uma nova empresa caso não exista uma empresa com o mesmo CNPJ/CNES."""
    empresa = crud.read_by_cnpj_cnes(db, emp.cnpj, emp.cnes)
    if empresa:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Empresa com este CNPJ/CNES já existe")
    return crud.create(db,emp)

@empresas_router.put("/{id}", response_model=schemas.EmpresaConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def update_empresa(id: int, empresa_data: schemas.EmpresaBase, db: Session = Depends(get_db)):
    """Atualiza uma empresa existente pelo ID."""
    empresa = crud.update(db, id, empresa_data)
    if empresa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Empresa com ID {id} não encontrada")
    return empresa

@empresas_router.delete("/{id}", response_model=schemas.EmpresaConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def delete_empresa(id: int, db: Session = Depends(get_db)):
    """Exclui uma empresa pelo ID."""
    empresa = crud.delete(db, id)
    if empresa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Empresa com ID {id} não encontrada")
    return empresa
