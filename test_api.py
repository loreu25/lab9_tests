import os

import requests


BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
TIMEOUT = 10


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["email"] == "Sincere@april.biz"


def test_create_user():
    payload = {"name": "Test User", "username": "testuser", "email": "test@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=TIMEOUT)

    assert response.status_code == 201
    assert "application/json" in response.headers["Content-Type"]

    user = response.json()
    assert user["id"] == 11
    assert user["name"] == payload["name"]
    assert user["username"] == payload["username"]
    assert user["email"] == payload["email"]


def test_update_user():
    payload = {"id": 1, "name": "Updated User", "username": "updateduser"}
    response = requests.put(f"{BASE_URL}/users/1", json=payload, timeout=TIMEOUT)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    user = response.json()
    assert user["id"] == payload["id"]
    assert user["name"] == payload["name"]
    assert user["username"] == payload["username"]
