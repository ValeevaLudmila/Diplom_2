import pytest
import requests
from urls import Url
from generators import email_generator, password_generator, name_generator
from data import TestData


@pytest.fixture
def create_user():
    """Фикстура для создания пользователя и последующего удаления."""
    email = email_generator()
    password = password_generator()
    name = name_generator()

    user_data = {"email": email, "password": password, "name": name}

    response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=user_data)
    token = response.json().get("accessToken")

    yield user_data, token

    if token:
        requests.delete(
            f'{Url.MAIN_URL}{Url.USER_PROFILE}',
            headers={"Authorization": token}
        )



@pytest.fixture
def generate_user_data():
    """Фикстура для генерации данных пользователя без создания"""
    return {
        "email": email_generator(),
        "password": password_generator(),
        "name": name_generator()
    }


@pytest.fixture
def setup_existing_user():
    """Фикстура для подготовки существующего пользователя"""
    user_data = {
        "email": TestData.EXISTING_USER_EMAIL,
        "password": TestData.EXISTING_USER_PASSWORD,
        "name": TestData.EXISTING_USER_NAME
    }

    try:
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=user_data)
        if response.status_code == 403:
            requests.post(f'{Url.MAIN_URL}{Url.LOGIN_USER}', json={
                "email": user_data["email"],
                "password": user_data["password"]
            })
    except requests.RequestException:
        pass

    return user_data
