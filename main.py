#!/usr/bin/env python3

from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/')
async def root():
    """
    Root elements
    """
    return {'message': 'Hello, World!'}

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {'item_id': item_id}

@app.get('/health')
def health():
    return {'errors': None}


if __name__ == '__main__':
    uvicorn.run(app)
