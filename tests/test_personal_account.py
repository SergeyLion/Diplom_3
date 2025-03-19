import allure
from data import BaseData as Bd
from locators.base_page_locators import HeaderLocators as Hl
from locators.recovery_password_page_locators import RecoveryLocators as Rl
from locators.personal_account_page_locators import PersonalAccountLocators as Pal
from pages.auth_page import AuthPage
from pages.personal_account_page import PersonalAccountPage


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title('Переход в личный кабинет по клику на кнопку "Личный кабинет"')
    @allure.description('Проверяем, что при клике на кнопку "Личный кабинет" происходит переход в личный кабинет')
    def test_click_personal_account_redirect(self, driver, create_user):
        data_create_user = create_user
        data_user = data_create_user.get("payload")
        username = data_user.get("email")
        password = data_user.get("password")
        auth_page = AuthPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        with allure.step("Открываем главную страницу"):
            auth_page.open(Bd.URL_STELLAR_BURGERS)

        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            auth_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Авторизуемся"):
            auth_page.auth_login(username, password)

        with allure.step("Переходим в личный кабинет"):
            personal_account_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Проверяем, что отображается вкладка 'Профиль'"):
            assert personal_account_page.check_is_displayed(Pal.TAB_PROFILER), "Вкладка 'Профиль' не отображается"

    @allure.title('Переход в раздел "История заказов"')
    @allure.description('Проверяем, что при переходе в раздел "История заказов" отображаются заказы пользователя')
    def test_navigate_to_order_history(self, driver, create_user_orders):
        data_create_user_orders = create_user_orders
        user_payload = data_create_user_orders.get("user_payload")
        username = user_payload.get("email")
        password = user_payload.get("password")
        auth_page = AuthPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        with allure.step("Открываем главную страницу"):
            auth_page.open(Bd.URL_STELLAR_BURGERS)

        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            auth_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Авторизуемся"):
            auth_page.auth_login(username, password)

        with allure.step("Переходим в личный кабинет"):
            personal_account_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Переходим в раздел 'История заказов'"):
            personal_account_page.click_element(Pal.TAB_HISTORY_ORDER)

        with allure.step("Проверяем, что количество заказов совпадает с ожидаемым"):
            list_orders = personal_account_page.find_elements(Pal.LIST_ORDERS_HISTORY)
            assert len(list_orders) == len(data_create_user_orders.get("orders")), \
                "Количество заказов не совпадает с ожидаемым"

    @allure.title('Выход из аккаунта')
    @allure.description('Проверяем, что при нажатии на кнопку "Выход" происходит выход из аккаунта')
    def test_logout_from_account(self, driver, create_user):
        data_create_user = create_user
        data_user = data_create_user.get("payload")
        username = data_user.get("email")
        password = data_user.get("password")
        auth_page = AuthPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        with allure.step("Открываем главную страницу"):
            auth_page.open(Bd.URL_STELLAR_BURGERS)

        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            auth_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Авторизуемся"):
            auth_page.auth_login(username, password)

        with allure.step("Переходим в личный кабинет"):
            personal_account_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Нажимаем на кнопку 'Выход'"):
            personal_account_page.click_element(Pal.TAB_EXIT)

        with allure.step("Проверяем, что отображается кнопка 'Войти'"):
            assert personal_account_page.check_is_displayed(Rl.BUTTON_ENTER), "Кнопка 'Войти' не отображается"