import allure
from data import BaseData as Bd
from locators.base_page_locators import HeaderLocators as Hl
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderPage
from locators.constructor_page_locators import ConstructorLocators as Cl
from pages.auth_page import AuthPage
from locators.list_orders_page_locators import ListOrdersLocators as Lol



@allure.feature("Основной функционал")
class TestBaseFunctionality:

    @allure.title('Переход в конструктор по клику на кнопку "Конструктор"')
    @allure.description('Проверяем, что при клике на кнопку "Конструктор" происходит переход в раздел конструктора')
    def test_click_constructor_redirect(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Открываем главную страницу"):
            constructor_page.open(Bd.URL_STELLAR_BURGERS)
        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            constructor_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)
        with allure.step("Нажимаем на кнопку 'Конструктор'"):
            constructor_page.click_element(Hl.BUTTON_CONSTRUCTOR)
        with allure.step("Проверяем, что отображается раздел 'Булки'"):
            assert constructor_page.check_is_displayed(Cl.TAB_BUN), "Раздел 'Булки' не отображается"

    @allure.title('Переход в ленту заказов по клику на кнопку "Лента заказов"')
    @allure.description('Проверяем, что при клике на кнопку "Лента заказов" происходит переход в раздел ленты заказов')
    def test_click_order_feed_redirect(self, driver):
        order_page = OrderPage(driver)
        with allure.step("Открываем главную страницу"):
            order_page.open(Bd.URL_STELLAR_BURGERS)
        with allure.step("Нажимаем на кнопку 'Лента заказов'"):
            order_page.click_element(Hl.BUTTON_LIST_ORDERS)
        with allure.step("Проверяем, что отображается заголовок ленты заказов"):
            assert order_page.check_is_displayed(Lol.HEADER_LIST_ORDERS), "Заголовок ленты заказов не отображается"

    @allure.title('Открытие модального окна при клике на ингредиент')
    @allure.description('Проверяем, что при клике на ингредиент открывается модальное окно с деталями')
    def test_ingredient_click_opens_modal(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Открываем главную страницу"):
            constructor_page.open(Bd.URL_STELLAR_BURGERS)
        with allure.step("Находим ингредиенты и кликаем на первый"):
            constructor_page.click_element(Cl.BURGER_INGREDIENTS)
        with allure.step("Проверяем, что модальное окно с деталями ингредиента отображается"):
            assert constructor_page.check_is_displayed(Cl.HEADER_MODAL_INGREDIENT), "Модальное окно с деталями ингредиента не отображается"

    @allure.title('Закрытие модального окна при клике на крестик')
    @allure.description('Проверяем, что модальное окно закрывается при клике на крестик')
    def test_ingredient_modal_closes_on_click(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Открываем главную страницу"):
            constructor_page.open(Bd.URL_STELLAR_BURGERS)
        with allure.step("Находим ингредиенты и кликаем на первый"):
            constructor_page.click_element(Cl.BURGER_INGREDIENTS)
            header_modal = constructor_page.find_element(Cl.HEADER_MODAL_INGREDIENT)
        with allure.step("Находим модальное окно и кликаем на крестик"):
            constructor_page.click_element(Cl.BUTTON_CLOSE_MODAL_INGREDIENT)
        with allure.step("Проверяем, что модальное окно больше не отображается"):
            constructor_page.invis_element(Cl.HEADER_MODAL_INGREDIENT)
            assert header_modal.is_displayed() == False, "Модальное окно не закрылось"

    @allure.title('Увеличение счётчика ингредиента при добавлении в заказ')
    @allure.description('Проверяем, что счётчик ингредиента увеличивается при добавлении его в заказ')
    def test_ingredient_counter_increases(self, driver):
        constructor_page = ConstructorPage(driver)
        with allure.step("Открываем главную страницу"):
            constructor_page.open(Bd.URL_STELLAR_BURGERS)
        with allure.step("Находим ингредиент и перетаскиваем в секцию заказа"):
            constructor_page.drag_and_drop_js(Cl.BURGER_INGREDIENTS, Cl.SECTION_ORDER)
        with allure.step("Проверяем, что счётчик ингредиента увеличился до 2"):
            counters_num = constructor_page.find_elements(Cl.COUNTER_NUM_INGREDIENTS)
            assert counters_num[0].text == "2", "Счётчик ингредиента не увеличился"

    @allure.title('Оформление заказа залогиненным пользователем')
    @allure.description('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_create_order(self, driver, create_user):
        data_create_user = create_user
        data_user = data_create_user.get("payload")
        username = data_user.get("email")
        password = data_user.get("password")
        auth_page = AuthPage(driver)
        constructor_page = ConstructorPage(driver)
        with allure.step("Открываем главную страницу"):
            auth_page.open(Bd.URL_STELLAR_BURGERS)
        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            auth_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)
        with allure.step("Авторизуемся"):
            auth_page.auth_login(username, password)
        with allure.step("Перетаскиваем ингредиент в секцию заказа"):
            constructor_page.drag_and_drop_js(Cl.BURGER_INGREDIENTS, Cl.SECTION_ORDER)
        with allure.step("Нажимаем кнопку 'Оформить заказ'"):
            constructor_page.click_element(Cl.BUTTON_CREATE_ORDER)
        with allure.step("Проверяем, что отображается сообщение об успешном создании заказа"):
            assert constructor_page.check_is_displayed(Cl.TEXT_SUCCESS_CREATE_ORDER), "Сообщение об успешном создании заказа не отображается"