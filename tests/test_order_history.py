import allure
from data import BaseData as Bd
from locators.base_page_locators import HeaderLocators as Hl
from pages.auth_page import AuthPage
from locators.order_history_page_locators import OrderHistoryLocators as Ohl
from locators.personal_account_page_locators import PersonalAccountLocators as Pal
from pages.order_feed_page import OrderPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title('Открытие модального окна с деталями заказа')
    @allure.description('Проверяем, что при клике на заказ открывается всплывающее окно с деталями')
    def test_click_order_opens_modal(self, driver):
        order_page = OrderPage(driver)
        with allure.step("Открываем главную страницу"):
            order_page.open(Bd.URL_STELLAR_BURGERS)
        with allure.step("Переходим в ленту заказов"):
            order_page.click_element(Hl.BUTTON_LIST_ORDERS)
        with allure.step("Кликаем на заказ"):
            order_page.click_element(Ohl.CARD_ORDER)
        with allure.step("Проверяем, что модальное окно с деталями заказа отображается"):
            assert order_page.check_is_displayed(Ohl.MODAL_ORDER), "Модальное окно с деталями заказа не отображается"


    @allure.title('Проверка отображения заказов пользователя в истории заказов')
    @allure.description('Проверяем, что заказы пользователя отображаются в разделе "История заказов"')
    def test_user_orders_in_order_history(self, driver, create_user_orders):
        # Получаем данные для авторизации
        data_create_user_orders = create_user_orders
        user_payload = data_create_user_orders.get("user_payload")
        username = user_payload.get("email")
        password = user_payload.get("password")

        # Инициализация страниц
        auth_page = AuthPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открываем главную страницу"):
            auth_page.open(Bd.URL_STELLAR_BURGERS)
        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            auth_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)
        with allure.step("Авторизуемся"):
            auth_page.auth_login(username, password)
        with allure.step("Переходим в личный кабинет"):
            order_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)
        with allure.step("Переходим в раздел 'История заказов'"):
            order_page.click_element(Pal.TAB_HISTORY_ORDER)

        with allure.step("Получаем список номеров заказов из истории"):
            history_order_elements = order_page.find_elements(Pal.NUMBER_ORDER)
            history_order_numbers = [element.text for element in history_order_elements]

        with allure.step("Проверяем, что список заказов в истории не пуст"):
            assert len(history_order_numbers) > 0, "Список заказов в истории пуст"

        with allure.step("Переходим в раздел 'Лента заказов'"):
            order_page.click_element(Hl.BUTTON_LIST_ORDERS)

        with allure.step("Проверяем, что все заказы из истории присутствуют в ленте заказов"):
            for order_number in history_order_numbers:
                assert order_page.search_number_order(order_number), f"Заказ {order_number} отсутствует в ленте заказов"



    @allure.title("Проверка отображения нового заказа в разделе 'В работе'")
    @allure.description("Проверяем, что новый заказ пользователя отображаются в разделе 'В работе'")
    def test_new_order_appears_in_progress(self, api_client, driver, login_user, create_list_ingredients):
        # Получаем данные пользователя и списки ингредиентов
        data_user = login_user
        user_payload = data_user.get("payload")
        username = user_payload.get("email")
        password = user_payload.get("password")
        list_ingredients = create_list_ingredients
        token_login = data_user.get("token")

        # Инициализация страниц
        auth_page = AuthPage(driver)
        order_page = OrderPage(driver)

        # Открываем страницу и авторизуемся
        with allure.step("Открываем главную страницу и авторизуемся"):
            auth_page.open(Bd.URL_STELLAR_BURGERS)
            auth_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)
            auth_page.auth_login(username, password)

        # Переходим в ленту заказов
        with allure.step("Переходим в раздел 'Лента заказов'"):
            order_page.click_element(Hl.BUTTON_LIST_ORDERS)

        # Создаем заказ
        number_order = order_page.create_order(list_ingredients=list_ingredients, token=token_login)


        # Проверяем, что номер заказа присутствует в списке
        with allure.step("Проверяем, что номер созданного заказа отображается в разделе 'В работе'"):
            assert order_page.search_number_in_progress(int(number_order)), \
                f"Заказ с номером {number_order} не найден в списке заказов в работе"


    @allure.title('Проверка увеличения счётчика заказов за сегодня')
    @allure.description('Проверяем, что счётчик заказов за сегодня увеличивается после создания нового заказа')
    def test_today_orders_counter_increases(self, api_client, driver, login_user, create_list_ingredients):
        # Получаем данные пользователя и списки ингредиентов
        data_user = login_user
        user_payload = data_user.get("payload")
        username = user_payload.get("email")
        password = user_payload.get("password")
        list_ingredients = create_list_ingredients
        token_login = data_user.get("token")

        # Инициализация страниц
        auth_page = AuthPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открываем главную страницу и авторизуемся"):
            auth_page.open(Bd.URL_STELLAR_BURGERS)
            auth_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)
            auth_page.auth_login(username, password)

        with allure.step("Переходим в раздел 'Лента заказов'"):
            order_page.click_element(Hl.BUTTON_LIST_ORDERS)

        with allure.step("Получаем текущее значение счётчика заказов за сегодня"):
            count_order_today = order_page.find_element(Ohl.COUNT_ORDERS_TODAY).text

        with allure.step("Создаем новый заказ"):
            order_page.create_order(list_ingredients=list_ingredients, token=token_login)

        with allure.step("Проверяем, что счётчик заказов за сегодня увеличился"):
            assert order_page.search_count_today(int(count_order_today)), "Счётчик заказов за сегодня не увеличился"

    @allure.title('Проверка увеличения счётчика заказов за все время')
    @allure.description('Проверяем, что счётчик заказов за все время увеличивается после создания нового заказа')
    def test_total_orders_counter_increases(self, api_client, driver, login_user, create_list_ingredients):
        # Получаем данные пользователя и списки ингредиентов
        data_user = login_user
        user_payload = data_user.get("payload")
        username = user_payload.get("email")
        password = user_payload.get("password")
        list_ingredients = create_list_ingredients
        token_login = data_user.get("token")

        # Инициализация страниц
        auth_page = AuthPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открываем главную страницу и авторизуемся"):
            auth_page.open(Bd.URL_STELLAR_BURGERS)
            auth_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)
            auth_page.auth_login(username, password)

        with allure.step("Переходим в раздел 'Лента заказов'"):
            order_page.click_element(Hl.BUTTON_LIST_ORDERS)

        with allure.step("Создаем новый заказ"):
            number_order = order_page.create_order(list_ingredients=list_ingredients, token=token_login)

        with allure.step("Проверяем, что счётчик заказов за все время увеличился"):
            assert order_page.search_count_all_time(number_order), "Счётчик заказов за все время не увеличился"

