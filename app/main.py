import uvicorn
from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run('app.main:app',
                reload=True,)




# python -m uvicorn app.main:app --reload
