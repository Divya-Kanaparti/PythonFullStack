from fastapi import FastAPI

app=FastAPI()


@app.get('/add/{a}{b}')
def add(a:int,b:int):
    return f"addition of {a} and {b} is {a+b}"

from typing import Optional
@app.get('/search')
def search(name:str,age:int):
    return {"msg":f"my name is{name} and age is {age}"}

@app.get('/greet/{name}/{age}')
def greet(name:str,age:int,city:str):
    return {"data":f"my name is {name},age is {age} and city is {city}"}   