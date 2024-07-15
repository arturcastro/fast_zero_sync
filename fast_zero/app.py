from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hi world!'}


@app.get('/hi', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hi():
    return '''<html><h3>Hi world!</h3></html>'''
