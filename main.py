from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "world"}  # we can return a dict, list, singular values as str, int, etc.


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/user/me")
async def read_user_me():
    return {"current_user": "This user is me!"}


@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"current_user": user_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/model/{model_name}")
async def read_model_name(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"Model name is:": model_name, "message": "Deep Learning FTW!"}
    elif model_name == ModelName.lenet:
        return {"Model name is:": model_name, "message": "LeCNN all the images"}
    else:
        return {"Model name is:": model_name, "message": "Have some residuals"}


