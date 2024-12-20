import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8050, log_level="info")
    #uvicorn.run("main:app", host="127.0.0.1", port=8050, log_level="info", reload=True)
