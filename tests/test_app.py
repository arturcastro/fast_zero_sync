from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # act (ação)

    assert response.status_code == HTTPStatus.OK  # assert (afirmação)
    assert response.json() == {'message': 'hi world!'}


def test_hi_deve_retornar_ok_e_hi_world(client):
    response = client.get('/hi')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<html><h3>Hi world!</h3></html>'


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            },
        ]
    }


def test_read_user(client):
    user_id = 1
    response = client.get(f'/users/{user_id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_update_user(client):
    id_ = 1

    response = client.put(f'/users/{id_}', json={
        'username': 'testusername2222',
        'email': 'test@test.com',
        'password': '123456',
        'id': id_,
    })

    assert response.json() == {
        'username': 'testusername2222',
        'email': 'test@test.com',
        'id': 1,
    }


def test_update_user_404(client):
    id_ = 99999
    response = client.put(f'/users/{id_}', json={
        'username': 'testusername2222',
        'email': 'test@test.com',
        'password': '123456',
        'id': id_,
    })
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_404(client):
    user_id = 99999
    response = client.delete(f'/users/{user_id}')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
