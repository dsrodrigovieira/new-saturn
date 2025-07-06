from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Indicador(Base):
    __tablename__ = "indicadores"

    id      = Column(Integer, primary_key=True, index=True)
    nome    = Column(String, index=True)
    valor   = Column(Float)
    unidade = Column(String)
    mes     = Column(String)

class Usuario(Base):
    __tablename__ = "usuarios"

    id      = Column(Integer, primary_key=True, index=True)
    login   = Column(String, index=True)
    senha   = Column(String)
    nome    = Column(String)
    email   = Column(String)
    status  = Column(String)