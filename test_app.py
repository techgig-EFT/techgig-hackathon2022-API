import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()

def test_healthcheck(client):
    resp = client.get('/')
    assert isinstance(resp.json, dict)
    assert resp.json.get('message')=='Hello from flask'

