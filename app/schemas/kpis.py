from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime

class KpiBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    dominio: Optional[str] = None
    unidade: Optional[str] = None
    meta: Optional[float] = None
    meta_descricao: Optional[str] = None
    sequencia: Optional[int] = None
    direcao_favoravel: Optional[Literal['C', 'D']] = None
    caminho_documentacao: Optional[str] = None
    ativo: bool = True
    dt_criacao: Optional[datetime] = None
    dt_atualizacao: Optional[datetime] = None

    class Config:
        from_attributes = True
        orm_mode = True

class Kpi(KpiBase):
    id: int

Kpis = List[Kpi]

class KpiConfirmaAlteracao(BaseModel):
    id: int
    titulo: str

    class Config:
        from_attributes = True
        orm_mode = True
