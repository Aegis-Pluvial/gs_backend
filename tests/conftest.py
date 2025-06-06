import pytest
from fastapi.testclient import TestClient
from gs_backend.main import app


# Monta o client de testes chamando a fixture do pytest
@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client
