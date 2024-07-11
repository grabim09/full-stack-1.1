from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id:int
    name:str
    age:int

DB:list[Person] = [
    Person(id=0,name='Agra',age=18),
    Person(id=1,name='Bima',age=20),
    Person(id=2,name='Yuda',age=22)
]

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/person')
def read_item():
    return DB

@app.get('/person/{person_id}')
def read_item(person_id:int):
    return {"person_id": person_id, "person": DB[person_id]}