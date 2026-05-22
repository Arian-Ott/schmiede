import pytest


def test_get_returns_true(client):
    response = client.get("/fake/returns_true")
    assert response.status_code == 200
    assert response.json() is True


def test_post_returns_what_came(client):
    payload = {"hello": "world"}
    response = client.post("/fake/returns_what_came", json=payload)
    assert response.status_code == 200
    assert response.json() == payload


def test_unknown_route_returns_404(client):
    response = client.get("/fake/does_not_exist")
    assert response.status_code == 404
