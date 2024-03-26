from typing import Union 

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates 

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )
    
@app.get("/about")
def home(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request}
    )
    
@app.get("/user/signin")
def login(request: Request):
    return templates.TemplateResponse(
        "signin.html", {"request": request}
    )
    
@app.get("/user/signup")
def signup(request: Request):
    return templates.TemplateResponse(
        "signup.html", {"request": request}
    )

