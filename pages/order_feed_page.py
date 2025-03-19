import allure
from pages.base_page import BasePage
from api_client.api_client import APIClient
from data import BaseData as Bd
from selenium.webdriver.common.by import By



class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Создаем заказ')
    def create_order(self, list_ingredients, token):
        headers = {"Authorization": token}
        api_client = APIClient(Bd.URL_API_STELLAR_BURGERS)
        # Формируем списки ингредиентов
        buns = list_ingredients["buns"]
        mains = list_ingredients["mains"]
        sauces = list_ingredients["sauces"]

        # Создаем заказ
        payload = {"ingredients": [buns[0], mains[0], sauces[0]]}

        # Отправляем запрос на создание заказа
        with allure.step("Создаем новый заказ через API"):
            response = api_client.post(Bd.ENDPOINT_CREATE_ORDER, data=payload, headers=headers)

        # Проверяем статус код ответа
        with allure.step("Проверяем, что заказ успешно создан"):
            assert response.status_code == 200, f"Ожидался статус код 200, но получен {response.status_code}"

        # Сохраняем данные созданного заказа
        order_data = response.json()
        with allure.step("Извлекаем номер заказа из ответа API"):
            number = order_data["order"]["number"]
            return number

    @allure.step('Ищет номер {number} заказа в списке заказов в работе.')
    def search_number_in_progress(self, number):
        """
        Ищет номер заказа в списке заказов в работе.

        :param number: Номер заказа для поиска.
        :return: True, если номер найден, иначе False.
        """
        try:
            locator = (By.XPATH, f"//ul[contains(@class,'OrderFeed_orderListReady')]/li[text()='{number}']")
            self.wait_for_load(locator)
            return True
        except:
            return False

    @allure.step('Ищет количество заказов за все время равных последнему созданному заказу {number}.')
    def search_count_all_time(self, number):
        """
                Ищет количество заказов равных последнему созданному заказу.

                :param number: Номер заказа для поиска.
                :return: True, если номер заказа равен счетчику, иначе False.
                """
        try:
            locator = (By.XPATH, f"//div[contains(@class,'undefined')]/p[text()='{number}']")
            self.wait_for_load(locator)
            return True
        except:
            return False

    @allure.step('Ищет количество заказов за сегодня.')
    def search_count_today(self, count_order_today):
        """
                        Ищет количество заказов за сегодня.

                        :param count_order_today: Количество заказов за сегодня.
                        :return: True, если номер заказа равен счетчику, иначе False.
                        """
        try:
            locator = (By.XPATH, f"//div/p[text()='{count_order_today +1}']")
            self.wait_for_load(locator)
            return True
        except:
            return False

    @allure.step('Проверяем, что заказ {number} есть в ленте заказа')
    def search_number_order(self, number):
        """
        Ищет количество заказов за сегодня.
        :param number: Количество заказов за сегодня.
        :return: True, если номер заказа равен счетчику, иначе False.
                                """
        try:
            locator = (By.XPATH, f"//div[contains(@class,'OrderHistory_textBox')]/p[text()='{number}']")
            self.wait_for_load(locator)
            return True
        except:
            return False