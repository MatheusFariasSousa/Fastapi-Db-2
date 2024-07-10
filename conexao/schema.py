
from sqlalchemy.orm import Mapped,mapped_column,registry
from sqlalchemy import DateTime,String
from datetime import datetime
from pydantic import BaseModel,field_validator
from fastapi import HTTPException
from typing import List

table_registry = registry()

@table_registry.mapped_as_dataclass
class Usuarios():
    __tablename__="Usuarios"
    
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True,init=False)
    nome:Mapped[str] = mapped_column(String(30))
    cpf:Mapped[str] = mapped_column(String(30))


class UsuarioInput(BaseModel):
    nome:str
    cpf:str

    @field_validator("cpf")
    def validar_cpf(cls,cpf:str):
        if len(cpf)!=11:
            raise ValueError("O cpf precisa de 11 digitos")
        
        for x in cpf:
            if not x.isnumeric():
                raise ValueError("O cpf aceita apenas numeros")
        return cpf

        



class UsuarioOutput(BaseModel):
    id:int
    nome:str
    cpf:str



    





