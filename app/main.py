from fastapi     import FastAPI
from app.routers import usuarios, empresas, kpis
from .database   import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Saturn Analytics API",
              description="Esta API fornece endpoints para gerenciar usuários e empresas da Saturn Analytics",
              version="0.1.0")
app.include_router(usuarios.usuarios_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(empresas.empresas_router, prefix="/empresas", tags=["Empresas"])
app.include_router(kpis.kpis_router, prefix="/kpis", tags=["Kpis"])

@app.get("/",include_in_schema=False)
def read_root():
    return {"message": "Saturn Analytics API online"}
