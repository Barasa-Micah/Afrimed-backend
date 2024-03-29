from typing import Union 

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates 
from forms import UserCreateForm


templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "root.html", {"request": request}
    )

@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )
    
@app.get("/about")
async def home(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request}
    )
    
# @app.get("/user/signin")
# async def login(request: Request):
#     return templates.TemplateResponse(
#         "signin.html", {"request": request}
#     )
    
# @app.get("/user/signup")
# async def signup(request: Request):
#     form = UserCreateForm(request)
#     await form.load_data()
#     print("submitted successfully")
#     if await form.is_valid():
#         # errors = ["Save to database"]
#         print("signup successfully")
#     else:
#         print("Error Form")
#         # errors = form.errors
    
#     return templates.TemplateResponse(
#         "signup.html", {
#             "request": request,
#             # "errors": errors
#             }
#     )

@app.get("/symptom_tracker")
async def symptom_tracker(request: Request):
    return templates.TemplateResponse(
        "symptom_tracker.html", {"request": request}
    )
    
    
# edu_resource
@app.get("/edu_resource")
async def edu_resource(request: Request):
    return templates.TemplateResponse(
        "edu_resource.html", {"request": request}
    )
    