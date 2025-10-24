import requests
import allure
import pytest
from urls import Url
from data import StatusCode, ResponseBody, TestData, Flags


class TestLoginUser:

    @allure.title('Успешный логин под существующим пользователем')
    def test_login_existing_user_success(self, setup_existing_user):
        user_data = setup_existing_user
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        
        with allure.step("Логин под существующим пользователем"):
            response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_USER}', json=login_data)
        
        assert response.status_code == StatusCode.OK
        assert response.json()[Flags.SUCCESS] == True
        
        response_data = response.json()
        assert Flags.ACCESS_TOKEN in response_data
        assert Flags.REFRESH_TOKEN in response_data
        assert Flags.USER_DATA in response_data
        
        # Проверяем данные пользователя
        user_response = response_data[Flags.USER_DATA]
        assert user_response["email"] == user_data["email"]
        assert user_response["name"] == user_data["name"]

    @allure.title('Ошибка при логине с неверными данными')
    def test_login_with_invalid_credentials_returns_error(self):
        login_data = {
            "email": TestData.NONEXISTENT_EMAIL,
            "password": TestData.WRONG_PASSWORD
        }
        
        with allure.step("Попытаться войти с неверными данными"):
            response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_USER}', json=login_data)
        
        assert response.status_code == StatusCode.UNAUTHORIZED
        assert response.json() == ResponseBody.LOGIN_INCORRECT_CREDENTIALS

    @allure.title('Ошибка при отсутствии поля для логина')
    @pytest.mark.parametrize('missing_field', ['email', 'password'])
    def test_login_missing_field_returns_error(self, setup_existing_user, missing_field):
        user_data = setup_existing_user
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        del login_data[missing_field]
        
        with allure.step(f"Логин без поля {missing_field}"):
            response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_USER}', json=login_data)
        
        assert response.status_code == StatusCode.UNAUTHORIZED
        assert response.json()[Flags.SUCCESS] == False