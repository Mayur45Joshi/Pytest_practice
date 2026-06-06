
import requests
import pytest

def test_get_users():
    r = requests.get("https://reqres.in/api/users?page=2")
    assert r.status_code == 200

def test_invalid_user():
    r = requests.get("https://reqres.in/api/users/23")
    assert r.status_code == 404
