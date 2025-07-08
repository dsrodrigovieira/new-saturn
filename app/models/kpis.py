from sqlalchemy     import Column, Integer, String, Boolean, DateTime, Float, CheckConstraint
from sqlalchemy.sql import func
from app.database   import Base

class Kpi(Base):
    __tablename__ = "kpis"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, unique=True, index=True)
    descricao = Column(String, nullable=True)
    dominio = Column(String, nullable=True)
    unidade = Column(String, nullable=True)
    meta = Column(Float, nullable=True)
    meta_descricao = Column(String, nullable=True)
    sequencia = Column(Integer, nullable=True)
    direcao_favoravel = Column(String, nullable=True)
    caminho_documentacao = Column(String, nullable=True)
    ativo = Column(Boolean, default=True)
    dt_criacao = Column(DateTime(timezone=True), server_default=func.now())
    dt_atualizacao = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    __table_args__ = (
        CheckConstraint("direcao_favoravel IN ('C', 'D')", name="ck_direcao_favoravel_allowed_values"),
    )