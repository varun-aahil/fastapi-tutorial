from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get('/customers/{customer_id}')
def viewCustomer(customer_id : int = Path(description='To access specific customer via an ID')):
    data = getData()

    target_idx = None

    for idx, customer in enumerate(data):
        if customer['id'] == customer_id :
            target_idx = idx
            break

    if target_idx != None :
        return data[target_idx]
    raise HTTPException(status_code= 404, detail='error : customer not found')


@app.get('/sort')
def sort_customers(sort_by: str = Query(...,description='Sort on amount or id'), order_by : str = Query('asc',description='asc or desc')) :

    if sort_by not in ['amount','id']:
        raise HTTPException(status_code= 400, detail='Invalid sort by field, select ONLY from amount or id')
    
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code= 400, detail='Invalid order by field,select ONLY from asc or desc')
    
    data = getData()

    order = True if order_by=='desc' else False
    sorted_data = sorted(data, key= lambda x: x.get(sort_by,0), reverse= order)
    return sorted_data