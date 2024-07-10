from fastapi import APIRouter,Depends,status,HTTPException
from conexao.conex import conect_depends
from sqlalchemy import select
from conexao.schema import Usuarios,UsuarioOutput,UsuarioInput
from sqlalchemy.orm import Session

router_sql = APIRouter(prefix="/sql")



@router_sql.get("/get_all",status_code=status.HTTP_200_OK)
def get_all(session:Session=Depends(conect_depends)):
    users= session.scalars(select(Usuarios)).all()
    return {"Users":users}


@router_sql.get("/get/{id}",status_code=status.HTTP_200_OK,response_model=UsuarioOutput)
def get_by_id(id:int,session:Session= Depends(conect_depends)):
    user = session.scalar(select(Usuarios).where(Usuarios.id == id))
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Nao existe esse id no banco")
    return user


@router_sql.post("/post",response_model=UsuarioOutput,status_code=status.HTTP_201_CREATED)
def add_usuario(user:UsuarioInput,session:Session=Depends(conect_depends)):
    pessoa = Usuarios(nome=user.nome,cpf=user.cpf)
    cpf_textado = session.scalar(select(Usuarios).where(Usuarios.cpf == pessoa.cpf))
    if cpf_textado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail= f"Esse cpf ja foi utilizado {cpf_textado.cpf}")
    session.add(pessoa)
    session.commit()
    session.refresh(pessoa)
    return pessoa



@router_sql.put("/put/{id}",response_model=UsuarioOutput,status_code=status.HTTP_200_OK)
def upddate_user(id:int,user:UsuarioInput,session:Session=Depends(conect_depends)):
    pessoa = Usuarios(nome=user.nome,cpf=user.cpf)
    user = session.scalar(select(Usuarios).where(Usuarios.id == id))
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Nao existe esse id no banco")
    cpf_textado = session.scalar(select(Usuarios).where(Usuarios.cpf == pessoa.cpf))
    if cpf_textado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail= f"Esse cpf ja foi utilizado {cpf_textado.cpf}")
    session
    user.cpf = pessoa.cpf
    user.nome= pessoa.nome
    session.commit()
    session.refresh(user)
    return user
    




    
@router_sql.delete("/delete/{id}",status_code=status.HTTP_200_OK)
def delete_user(id:int,session:Session=Depends(conect_depends)):
    user = session.scalar(select(Usuarios).where(Usuarios.id == id))
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Nao existe esse id no banco")
    session.delete(user)
    session.commit()
    return user

@router_sql.get("/teste")
def testanto_apenas():
    return "Funciono"




        
        
        