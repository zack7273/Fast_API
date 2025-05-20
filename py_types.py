# from typing import union
from fastapi import FastAPI

app = FastAPI()

def full_name(first_name: str, last_name: str) -> str:
    return f'{first_name.capitalize()} {last_name.capitalize()}'


first_name = "Johny"
last_name = "cins"



@app.get('/full_name')
def name(first_name: str, last_name: str):
    return {"full_name": full_name(first_name, last_name)}


