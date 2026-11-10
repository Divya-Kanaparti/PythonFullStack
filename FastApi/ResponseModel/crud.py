from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel


app=FastAPI()

books=[
    {'bid':1,
     'bname':'python',
     'author':'ravi',
     'pdate':'19-10-1995'},
     {'bid':2,
          'bname':'java',
          'author':'kavya',
          'pdate':'10-09-1999'}
]

# api for retrive all books
@app.get('/books')
def get_books():
    return books

# API to retrieve a book based on ID
@app.get('/book/{id}')
def get_bookbyid(id: int):
    for b in books:
        if b['bid'] == id:
            return b

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book id {id} is not found"
    )

# post request

class Book(BaseModel):
    bid:int
    bname:str
    author:str
    pdate:str

@app.post('/book')
def add_book(book:Book):
    newbook=book.model_dump()
    books.append(newbook)
    return {"message":"book added successfully..."}


# put request: update the resource based on id

class Updatebook(BaseModel):
    bname:str
    author:str
    pdate:str

@app.put('/book/{id}')
def updatebook(id:int,updatebook:Updatebook):
    for b in books:
        if b['bid']==id:
            b['bname']=updatebook.bname
            b['author']=updatebook.author
            b['pdate']=updatebook.pdate
            return {"message":f"book id {id} is updated"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"book id {id} is not found")

# delete request 

@app.delete('/book/{id}')
def deletebook(id:int):
    for b in books:
        if b['bid']==id:
            books.remove(b)
            return {"message":f"book id {id} is removed"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book id {id} is not found")
