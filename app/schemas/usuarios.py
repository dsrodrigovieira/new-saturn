from pydantic import BaseModel
from typing import List
from datetime import datetime

class UsuarioBase(BaseModel):
    login: str
    senha: str
    nome_completo: str
    empresa_id: int
    email: str
    dt_criacao: datetime | None = None
    ativo: bool = True
    dt_atualizacao: datetime | None = None
    ultimo_login: str | None = None

    class Config:
        from_attributes = True
        orm_mode = True    

class Usuario(UsuarioBase):
    id: int

Usuarios = List[UsuarioBase]

class UsuarioConfirmaAlteracao(BaseModel):
    id: int
    login: str

    class Config:
        from_attributes = True
        orm_mode = True
        