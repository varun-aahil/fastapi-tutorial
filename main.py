from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'message' : "Hello World"}

@app.get('/about')
def aboutInfo():
    return {'message' : 'Hello this is a test demo from varun'}