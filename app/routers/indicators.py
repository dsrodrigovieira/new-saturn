from fastapi          import APIRouter, Depends
from sqlalchemy.orm   import Session
from app              import crud, schemas, models
from app.database     import SessionLocal, engine
from app.dependencies import get_db


models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/", response_model=list[schemas.Indicador])
def list_indicadores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_indicadores(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Indicador)
def create_indicador(ind: schemas.IndicadorCreate, db: Session = Depends(get_db)):
    return crud.create_indicador(db, ind)
