from fastapi import FastAPI,Request,Form
import mysql.connector
from fastapi.templating import Jinja2Templates

app=FastAPI()

def get_connection():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='collegedb'
    )
    return conn

templates=Jinja2Templates(directory='templates')

# api for get data from db send to html page

@app.get('/')
def Students(request:Request):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("select * from student")
    students=cursor.fetchall()
    if not students:
        cursor.close()
        return {"message":f"no student data found"}
    cursor.close()
    return templates.TemplateResponse(
        request=request,
        name='view.html',
        context={'students':students}
    )

# api for diplay register page

@app.get('/register')
def Register(request:Request):
    return templates.TemplateResponse(
        request=request,
        name='register.html',
        context={}
    )

# api for get data from form and stored in db
@app.post('/addstudent')
def Addstudent(request:Request,name:str=Form(...),city:str=Form(...),
               marks:float=Form(...),age:int=Form(...)):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("""insert into student(sid,name,city,marks,age) 
    values(%s,%s,%s,%s,%s)""",(id,name,city,marks,age))
    con.commit()
    cursor.close()
    return {"message":"student added successfully"}