from app import create_app
from flask import url_for

import pytest

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SERVER_NAME': 'localhost',
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_home(app, client):
    with client.session_transaction() as session:
        session['nickname'] = 'random'
    with app.app_context():
        response = client.get(url_for('rps.home'))
    assert response.status_code == 302

def test_registration(app, client):
    from json import dumps
    data = {'nickname': 'random'}
    with app.app_context():
        result = client.post(url_for('rps.game'), data=dumps(data))
    assert result.status_code == 200

def test_incorrect_input(app, client):
    with client.session_transaction() as session:
        session['nickname'] = 'random'
        session['score'] = 0
    with app.app_context():
        response = client.get(f"{url_for('rps.game')}?choice=random")
    assert response.status_code == 200


def test_game(app, client):
    from RPS.routes import game_result
    options = game_result.keys()
    with client.session_transaction() as session:
        session['nickname'] = 'random'
        session['score'] = 50
    for option in options:
        with app.app_context():
            result = client.get(f"{url_for('rps.game')}?choice={option}")
        assert result.status_code == 200

def test_logout(app, client):
    with client.session_transaction() as session:
        session['nickname'] = 'random'
        session['score'] = 50
    with app.app_context(), app.test_request_context():
        response = client.get(url_for('rps.logout'), follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == url_for('rps.home')
