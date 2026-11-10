from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

# request model
class EmployeeRequest(BaseModel):
    eid:int
    ename:str
    email:str
    dept:str
    salary:float
    password:str

# response Model
class EmployeeResponse(BaseModel):
    eid:int
    ename:str
    email:str
    dept:str
    salary:float


# POST: API
@app.post('/employee',response_model=EmployeeResponse)
def add_employee(employee:EmployeeRequest):
    return {
        "eid":employee.eid,
        "ename":employee.ename,
        "email":employee.email,
        "dept":employee.dept,
        "salary":employee.salary,
        "password":employee.password
    }