from fastapi              import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm       import Session
from app.schemas.usuarios import UsuarioBase, UsuarioConfirmaAlteracao
from app.crud.usuarios    import read_all, read_one, create, delete
from app.dependencies     import get_db
from typing               import List

usuarios_router = APIRouter()

@usuarios_router.get("/", response_model=List[UsuarioBase])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return read_all(db, skip=skip, limit=limit)

@usuarios_router.get("/{id}", response_model=UsuarioBase)
def read_usuario(id: int, db: Session = Depends(get_db)):
    usuario = read_one(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {id} não encontrado")
    return usuario

@usuarios_router.post("/", response_model=UsuarioConfirmaAlteracao, status_code=status.HTTP_201_CREATED)
def create_usuario(ind: UsuarioBase, db: Session = Depends(get_db)):
    return create(db, ind)

@usuarios_router.delete("/{id}", response_model=UsuarioConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def delete_usuario(id: int, db: Session = Depends(get_db)):
    usuario = delete(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {id} não encontrado")
    return usuario
