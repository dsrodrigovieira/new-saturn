from sqlalchemy     import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database   import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, unique=True, index=True)
    cnes = Column(Integer, unique=True, index=True)
    razao = Column(String)
    fantasia = Column(String)
    cep = Column(String)
    numero_endereco = Column(String, nullable=True)
    site = Column(String, nullable=True)
    telefone = Column(String)
    email = Column(String)
    dt_criacao = Column(DateTime(timezone=True), server_default=func.now())
    ativo = Column(Boolean, default=True)
    dt_atualizacao = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)    

    usuarios = relationship("Usuario", back_populates="empresa")