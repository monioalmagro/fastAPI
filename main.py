from fastapi import FastAPI
from typing import Optional
from modelName import ModelName
from db import fake_items_db




app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Hello World"}

""" @app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id":item_id} """

""" @app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id":item_id} """

@app.get("/users/me")
async def read_user_me():
    return {"user_id":"the current user"}

@app.get("/user/{user_id}")
async def read_user(user_id):
    return {"user_id":user_id}

@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name":model_name,"message":"Deep Learning FWT!"}
    if model_name == ModelName.lenet:
        return {"model_name":model_name,"message":"LeCNN all the images"}
    return {"model_name":model_name,"message":"Have some residuals."}

""" @app.get("/items/")#        ---------------------------->        http://127.0.0.1:8000/items/?skip=0&limit=2
async def read_item(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id} """

""" @app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item """

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item