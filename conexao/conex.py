from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session,sessionmaker

from os import getenv

from dotenv import load_dotenv

load_dotenv()

db_url= getenv("DB_URL")




engine = create_engine(db_url)


def conect_depends():
    with Session(engine) as session:
        yield session

teste_engine=sessionmaker(bind=engine)




  
