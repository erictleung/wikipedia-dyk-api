#!/usr/bin/env python3

from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title='Wikipedia Did You Know KPI',
    description='REST API for accessing Did You Know on Wikipedia since 2004',
    version='1.0.0'
)

@app.get(
    '/',
    summary='Base check',
    description='Base check that API is working'
)
async def root():
    return {'message': 'Hello, World!'}

@app.get(
    '/all',
    summary='Get all items',
    description='Retrieve all Did You Know quotes and date information',
    tags=['All']
)
async def get_all():
    return {'message': 'Hello, World!'}

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {'item_id': item_id}

@app.get('/health')
def health():
    return {'errors': None}


if __name__ == '__main__':
    uvicorn.run(app)
