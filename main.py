from fastapi import FastAPI
import json
app = FastAPI()

def getData():
    with open('test.json', 'r') as f:
        return json.load(f)

@app.get('/')
def hello():
    return {'message' : 'This is a Loan Managment System API'}

@app.get('/about')
def aboutInfo():
    return {'message' : 'This is an API to manage your customers loans'}

@app.get('/customers')
def getUsers():
    data = getData()
    return data