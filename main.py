from fastapi import FastAPI

app = FastAPI()

@app.post('/login')
async def login(username: str):
    return {"username": username}
