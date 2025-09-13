from fastapi import FastAPI
app = FastAPI()


@app.get("/blog")
def index(limit = 10,published:bool= True):
    if(published):
        return {'data': f'{limit} published blog list from the database'}
    else:
        return {"data": f'{limit} unpublished blog list from the database'}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'All are unpublished'}

@app.get("/blog/{item_id}")
async def user(item_id:str):
    return {'data': item_id}

@app.get("/blog/{item_id}/comments")
def comments(item_id):
    return{'data':{'1','2'}}
