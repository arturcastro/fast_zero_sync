from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange (organização)

    response = client.get('/')  # act (ação)

    # assert (afirmação)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hi'}


def test_html_hi_deve_retornar_ok_e_ola_mundo_html():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h3>Hi!</h3>'
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
