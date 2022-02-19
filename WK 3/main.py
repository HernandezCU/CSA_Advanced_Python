from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
import uvicorn
from CSV_Example import *


data = APIRouter(prefix="/data")

app = FastAPI()
x = import_data()
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1>Welcome</h1>
    <body>Docs can be found at /docs</body>
    """


@data.get("/get_id")
def get_by_id(id: int):
    z = find_by_id(x, id)
    if z != None:
        return {
            "code": 200,
            "message": "success",
            "data": z
        }
    else:
        return {
            "code": 422,
            "message": "id not found",
            "data": z
        }




@data.get("/get_firstname")
def get_by_first(first_name: str):

    return 0


@data.get("/get_lastname")
def get_by_last(last_name: str):

    return 0


@data.get("/get_email")
def get_by_email(email: str):

    return 0


@data.get("/get_position")
def get_by_position(position: str):

    return 0


@data.get("/get_department")
def get_by_department(department: str):

    return 0





app.include_router(data)

if __name__=='__main__':
    uvicorn.run("main:app", host="localhost", reload=True)


"""
Open a new terminal window and run: ipconfig
scroll to botton and find your IPV4 Address
"""