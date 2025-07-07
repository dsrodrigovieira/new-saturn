from fastapi              import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm       import Session
from app.schemas.empresas import EmpresaBase, EmpresaConfirmaAlteracao
from app.crud.empresas    import read_all, read_one, create, delete
from app.dependencies     import get_db
from typing               import List

empresas_router = APIRouter()

@empresas_router.get("/", response_model=List[EmpresaBase])
def read_empresas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return read_all(db, skip=skip, limit=limit)

@empresas_router.get("/{id}", response_model=EmpresaBase)
def read_empresa(id: int, db: Session = Depends(get_db)):
    empresa = read_one(db, id)
    if empresa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Empresa com ID {id} não encontrado")
    return empresa

@empresas_router.post("/", response_model=EmpresaConfirmaAlteracao, status_code=status.HTTP_201_CREATED)
def create_empresa(ind: EmpresaBase, db: Session = Depends(get_db)):
    return create(db, ind)

@empresas_router.delete("/{id}", response_model=EmpresaConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def delete_empresa(id: int, db: Session = Depends(get_db)):
    empresa = delete(db, id)
    if empresa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Empresa com ID {id} não encontrado")
    return empresa
