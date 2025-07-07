from pydantic import BaseModel
from typing import List
from datetime import datetime

class EmpresaBase(BaseModel):
    cnpj: str
    cnes: int
    razao: str
    fantasia: str
    endereco: str
    site: str
    telefone: str
    email: str
    dt_criacao: datetime | None = None
    ativo: bool = True
    dt_atualizacao: datetime | None = None

    class Config:
        from_attributes = True
        orm_mode = True

Empresas = List[EmpresaBase]

class EmpresaConfirmaAlteracao(BaseModel):
    id: int
    cnpj: str

    class Config:
        from_attributes = True
        orm_mode = True


