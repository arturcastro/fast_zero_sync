from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange (organização)

    response = client.get('/')  # act (ação)

    assert response.status_code == HTTPStatus.OK  # assert (afirmação)
    assert response.json() == {'message': 'hi world!'}


def test_hi_deve_retornar_ok_e_hi_world():
    client = TestClient(app)

    response = client.get('/hi')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<html><h3>Hi world!</h3></html>'