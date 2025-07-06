from pydantic import BaseModel

class IndicadorBase(BaseModel):
    nome: str
    valor: float
    unidade: str
    mes: str

class IndicadorCreate(IndicadorBase):
    pass

class Indicador(IndicadorBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True

class UsuarioBase(BaseModel):
    id: int | None = None
    login: str
    senha: str
    nome: str
    email: str
    status: str

class UsuarioCreate(UsuarioBase):
    pass

    class Config:
        from_attributes = True
        orm_mode = True

class UsuarioCreateConfirmation(BaseModel):
    id: int
    login: str

    class Config:
        from_attributes = True
        orm_mode = True

class UsuarioDelete(BaseModel):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True

class UsuarioDeleteConfirmation(BaseModel):
    id: int
    login: str

    class Config:
        from_attributes = True
        orm_mode = True

class Usuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True