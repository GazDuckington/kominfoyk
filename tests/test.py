import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


client = TestClient(app)


@pytest.mark.asyncio
async def test_login_success(mocker):
    # Mock the database fetchrow function
    mock_user = {
        "id": 1,
        "username": "testuser",
        "level": "user",
        "password": "testpass",
    }
    mocker.patch("your_module.connect_to_db", return_value="mock_database_connection")
    mocker.patch("your_module.fetchrow", return_value=mock_user)

    response = client.post(
        "/login/", data={"username": "testuser", "password": "testpass"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "true"
    assert response.json()["user_id"] == 1
    assert response.json()["level"] == "user"


@pytest.mark.asyncio
async def test_login_invalid_credentials():
    response = client.post(
        "/login/", data={"username": "wronguser", "password": "wrongpass"}
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Invalid credentials"
