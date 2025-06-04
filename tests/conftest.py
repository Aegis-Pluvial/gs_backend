import pytest
from fastapi.testclient import TestClient
from gs_backend.main import app


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client
