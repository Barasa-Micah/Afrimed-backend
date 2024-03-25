from pydantic import BaseModel
from fastapi import FastAPI 

app = FastAPI()

# class UserData(BaseModel):
    # name: str 
    # age: int 
    # stress_level: str 
    
@app.post('/user')
async def get_user(name:str, age:int, stress_level:str):
    return {
        "username": name, 
        "age": age,
        "stress_level": stress_level
        }  
