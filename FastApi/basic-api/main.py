from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def Home():
    return {"message":"Welcome to fastapi  learning"}