from fastapi import FastAPI
from tortoise.contrib .fastapi import register_tortoise
from models import *

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hola!"}

@app.post("/register")
async def user_registration(user: user_pydanticIn):
    user_info =  user.dict(exclude_unset=True)
    user_info["password"] = 

register_tortoise(
    app, 
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
