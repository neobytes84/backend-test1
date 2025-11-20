from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_author():
    resp = client.post("/authors/", json={"name": "Pablo Neruda"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Pablo Neruda"
    assert "id" in data
