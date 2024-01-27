from pytest import fixture
from fastapi.testclient import TestClient
from app.main import app

@fixture(scope="function")
def client():
    with TestClient(app=app, base_url="http://test") as client:
        yield client