from fastapi          import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm   import Session
from app              import crud, schemas, models
from app.database     import SessionLocal, engine
from app.dependencies import get_db

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/", response_model=list[schemas.Usuario])
def list_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_usuarios(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.Usuario)
def get_usuario(id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {id} não encontrado")
    return usuario

@router.post("/", response_model=schemas.UsuarioCreateConfirmation, status_code=status.HTTP_201_CREATED)
def create_usuario(ind: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db, ind)

@router.delete("/{id}", response_model=schemas.UsuarioDeleteConfirmation, status_code=status.HTTP_202_ACCEPTED)
def delete_usuario(id: int, db: Session = Depends(get_db)):
    usuario = crud.delete_usuario(db, id)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com ID {id} não encontrado")
    return usuario
