from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session,sessionmaker
from conexao.schema import table_registry,Usuarios



engine = create_engine("sqlite:///database.db")


def conect_depends():
    with Session(engine) as session:
        yield session

teste_engine=sessionmaker(bind=engine)




  
