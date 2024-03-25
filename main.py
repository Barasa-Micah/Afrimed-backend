from fastapi import FastAPI

app = FastAPI()

@app.post('/login')
async def login(username: str):
    return {"username": username}

@app.post('/quizzes')
async def quizes(game: str):
    return {"username": game}