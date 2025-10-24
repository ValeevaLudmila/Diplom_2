import requests
import allure
import pytest
from urls import Url
from data import StatusCode, ResponseBody, TestData, Flags


class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией') # Баг: ожидается 200, получаем 400
    def test_create_order_with_auth_success(self, create_user):
        user_data, token = create_user
        order_data = {
            "ingredients": TestData.VALID_INGREDIENTS
        }
        
        with allure.step("Создать заказ с авторизацией"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.CREATE_ORDER}', 
                json=order_data,
                headers={"Authorization": token}
            )
        
        assert response.status_code == StatusCode.OK
        assert response.json()[Flags.SUCCESS] == True
        assert Flags.NAME in response.json()
        assert Flags.ORDER_DATA in response.json()
        
        order_response = response.json()[Flags.ORDER_DATA]
        assert "number" in order_response

    @allure.title('Ошибка при создании заказа без авторизации') # Баг: ожидается 401, получаем 400
    def test_create_order_without_auth_returns_error(self):
        order_data = {
            "ingredients": TestData.VALID_INGREDIENTS
        }
        
        with allure.step("Попытаться создать заказ без авторизации"):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
        
        assert response.status_code == StatusCode.UNAUTHORIZED
        assert response.json() == ResponseBody.UNAUTHORIZED

    @allure.title('Ошибка при создании заказа без ингредиентов') # Баг: сервер возвращает HTML вместо JSON
    def test_create_order_without_ingredients_returns_error(self, create_user):
        user_data, token = create_user
        order_data = {
            "ingredients": []
        }
        
        with allure.step("Создать заказ без ингредиентов"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.CREATE_ORDER}', 
                json=order_data,
                headers={"Authorization": token}
            )
        
        assert response.status_code == StatusCode.BAD_REQUEST
        assert response.json() == ResponseBody.INGREDIENTS_REQUIRED

    @allure.title('Ошибка при создании заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredient_hash_returns_error(self, create_user):
        user_data, token = create_user
        order_data = {
            "ingredients": [TestData.INVALID_INGREDIENT_HASH]
        }
        
        with allure.step("Создать заказ с неверным хешем ингредиентов"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.CREATE_ORDER}', 
                json=order_data,
                headers={"Authorization": token}
            )
        
        assert response.status_code == StatusCode.INTERNAL_SERVER_ERROR
        assert response.json()[Flags.SUCCESS] == False