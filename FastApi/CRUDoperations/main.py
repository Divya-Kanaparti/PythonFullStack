from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
# import connector
import mysql.connector


app=FastAPI()


# establish connection bt python app and mysql db
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='collegedb'
)


# api for check connecton
@app.get('/connection') # http://127.0.0.1:8000/connection
def connectioncheck():
    return {"message":"DB connection is success..."}




# api for retrive data from db
@app.get('/students')
def getstudents():
    print("start")
    # create the cursor object
    cursor=conn.cursor(dictionary=True)
    cursor.execute("select * from student")
    # fetch the data from db
    result=cursor.fetchall()
    print("data is:",result)
    if not result:
        cursor.close()
        return {"message":"no data found"}
    cursor.close()
    return result


# api for get data by using student id


@app.get('/student/{id}') # http://127.0.0.1:8000/student/1
def getstudentbyid(id:int):
    cursor=conn.cursor(dictionary=True)
    cursor.execute("select * from student where sid=%s",(id,))
    result=cursor.fetchone()
    if not result:
        cursor.close()
        return {"message":f"student id {id} is not found"}
    cursor.close()
    return result


# api for post request: adding the student
class AddStudent(BaseModel):
    sname:str
    scity:str
    smarks:float
    sage:int


@app.post('/student')
def addstudent(addstudent:AddStudent):
    cursor=conn.cursor()
    cursor.execute("""insert into student(sname,scity,smarks,sage) values(%s,%s,%s,%s)""",
                   (addstudent.sname,addstudent.scity,addstudent.smarks,addstudent.sage))
    conn.commit()
    cursor.close()
    return {'message':"Student added successfully..."}


# api for delete request
@app.delete('/student/{sid}')
def deletestudent(sid:int):
    cursor=conn.cursor()
    cursor.execute("select * from student where id=%s",(sid,))
    result=cursor.fetchone()
    if  not result:
        cursor.close()
        return {"message":f"student id {sid} is not found"}
    cursor.execute("delete from student where id=%s",(sid,))
    conn.commit()
    cursor.close()
    return {"message":f"student id {sid} is deleted"}



