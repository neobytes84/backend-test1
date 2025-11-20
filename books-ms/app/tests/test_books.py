from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_book():
    resp = client.post("/books/", json={"title": "La Ilíada"})
    assert resp.status_code == 201
    body = resp.json()
    assert body["title"] == "La Ilíada"
    assert "id" in body
