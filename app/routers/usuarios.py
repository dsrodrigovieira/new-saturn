from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import usuarios as schemas
from app.crud import usuarios as crud
from app.dependencies import get_db
from typing import List

usuarios_router = APIRouter()

@usuarios_router.get("/", response_model=List[schemas.UsuarioBase])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retorna uma lista de usuários com paginação."""
    return crud.read_all(db, skip=skip, limit=limit)

@usuarios_router.get("/{id}", response_model=schemas.UsuarioBase)
def read_usuario(id: int, db: Session = Depends(get_db)):
    """Retorna um usuário específico pelo ID."""
    usuario = crud.read_one(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {id} não encontrado")
    return usuario

@usuarios_router.post("/", response_model=schemas.UsuarioConfirmaAlteracao, status_code=status.HTTP_201_CREATED)
def create_usuario(usr: schemas.UsuarioBase, db: Session = Depends(get_db)):
    """Cria um novo usuário caso não exista um usuário com o mesmo login."""
    usuario = crud.read_by_login(db, usr.login)
    if usuario:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Usuário com login '{usr.login}' já existe")
    return crud.create(db,usr)    

@usuarios_router.put("/{id}", response_model=schemas.UsuarioConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def update_usuario(id: int, usr: schemas.UsuarioBase, db: Session = Depends(get_db)):
    """Atualiza um usuário existente pelo ID."""
    usuario = crud.update(db, id, usr)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {id} não encontrado")
    return usuario

@usuarios_router.delete("/{id}", response_model=schemas.UsuarioConfirmaAlteracao, status_code=status.HTTP_202_ACCEPTED)
def delete_usuario(id: int, db: Session = Depends(get_db)):
    """Exclui um usuário pelo ID."""
    usuario = crud.delete(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {id} não encontrado")
    return usuario
