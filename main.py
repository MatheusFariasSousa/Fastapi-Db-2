from fastapi import FastAPI

from sql_routes.sql_route import router_sql


app = FastAPI()




@app.get("/index")
def hello_world():
    return "Health-Check"

app.include_router(router=router_sql)