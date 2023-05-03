from website import create_app
from flask import session
import pytest
import sqlite3


con = sqlite3.connect("./instance/database.db")
cur = con.cursor()


def test_home_page(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b'Email Address' in response.data
    assert b'Password' in response.data
    assert b'Login' in response.data
    assert b'<button type="Submit" class=\'btn btn-primary\'>Sign in</button>' in response.data


def test_signup_request_success(client):
    response = client.post("/sign-up", data={
        "email": "unitedunited2@hotmail.com",
        "firstName":'testFirstNameUnited2',
        "password1":'United1234',
        "password2":'United1234'

    })

    assert response.status_code == 200



def test_login_request_success(client):
    with client:
        client.post("/login", data={
            "email": "unitedunited2@hotmail.com",
            "password":'United1234'

        })
    
        assert session["_user_id"] == '1'


