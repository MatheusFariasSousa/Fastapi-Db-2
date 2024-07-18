
import pytest

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from main import app

from conexao.conex import conect_depends
from conexao.schema import table_registry,Usuarios

from fastapi.testclient import TestClient



@pytest.fixture
def client(session):
    def conect_depends_override():
        return session

    with TestClient(app=app) as client:
        app.dependency_overrides[conect_depends] = conect_depends_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user=Usuarios("Matheus","12345678910")
        session.add(user)
        session.commit()
        session.refresh(user)
        yield session

    table_registry.metadata.drop_all(engine)

@pytest.fixture
def user(session):
    user=Usuarios("Matheus","123456789")
    session.add(user)
    session.commit()
    session.refresh(user)
    




    


    



    


    
    
    
    


    