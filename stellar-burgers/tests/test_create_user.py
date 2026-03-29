import requests
import allure
import pytest
from urls import Url
from data import StatusCode, ResponseBody, Flags


class TestCreateUser:

    @allure.title('Успешное создание уникального пользователя')
    def test_create_unique_user_success(self, create_user):
        user_data, token = create_user

        with allure.step("Создать уникального пользователя"):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=user_data)

        assert response.status_code == StatusCode.OK
        assert response.json()[Flags.SUCCESS] is True

        response_data = response.json()
        assert Flags.ACCESS_TOKEN in response_data
        assert Flags.REFRESH_TOKEN in response_data
        assert Flags.USER_DATA in response_data

        user_response = response_data[Flags.USER_DATA]
        assert user_response["email"] == user_data["email"]
        assert user_response["name"] == user_data["name"]

    @allure.title('Ошибка при создании уже зарегистрированного пользователя')
    def test_create_existing_user_returns_error(self, setup_existing_user):
        existing_user_data = setup_existing_user

        with allure.step("Попытаться создать уже существующего пользователя"):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=existing_user_data)

        assert response.status_code == StatusCode.FORBIDDEN
        assert response.json() == ResponseBody.USER_ALREADY_EXISTS

    @allure.title('Ошибка при отсутствии обязательного поля')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_error_when_required_field_missing(self, generate_user_data, missing_field):
        user_data = generate_user_data.copy()
        del user_data[missing_field]

        with allure.step(f"Создать пользователя без поля {missing_field}"):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=user_data)

        assert response.status_code == StatusCode.FORBIDDEN
        assert response.json() == ResponseBody.REQUIRED_FIELDS_MISSING
