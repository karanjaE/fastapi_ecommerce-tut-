from fastapi import FastAPI
from tortoise.contrib .fastapi import register_tortoise
from models import *
from authentication import *

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hola!"}

@app.post("/register")
async def user_registration(user: user_pydanticIn):
    user_info =  user.dict(exclude_unset=True)
    user_info["password"] = get_hashed_password(user_info["password"])
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)
    return{
        "status": "ok",
        "data": f"Hello {new_user.username}. Check your email for a confirmation"
    }

register_tortoise(
    app, 
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
