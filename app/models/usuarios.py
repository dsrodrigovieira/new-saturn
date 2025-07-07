from sqlalchemy     import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database   import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, index=True)
    senha = Column(String)
    nome_completo = Column(String)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    email = Column(String)
    dt_criacao = Column(DateTime(timezone=True), server_default=func.now())
    ativo = Column(Boolean, default=True)
    dt_atualizacao = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    ultimo_login = Column(DateTime(timezone=True), nullable=True)

    empresa = relationship("Empresa", back_populates="usuarios")