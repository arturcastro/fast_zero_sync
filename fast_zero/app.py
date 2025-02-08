from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hi', 'batata': 'frita'}


@app.get('/html', response_class=HTMLResponse)
def html_hi():
    return '<h3>Hi!</h3>'
