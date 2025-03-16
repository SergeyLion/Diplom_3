import allure
from data import BaseData as Bd
from locators.base_page_locators import HeaderLocators as Hl
from pages.auth_page import AuthPage
from locators.recovery_password_page_locators import RecoveryLocators as Rl


@allure.feature("Авторизация")
@allure.story("Страница восстановления пароля пользователя")
class TestRecoveryPassword:

    @allure.title('Переход на страницу "Восстановления пароля"')
    @allure.description('Переходим на форму восстановления и проверяем наличие кнопки "Восстановить"')
    def test_recover_link(self, driver):
        with allure.step("Открываем страницу магазина"):
            recovery_page = AuthPage(driver)
            recovery_page.open(Bd.URL_STELLAR_BURGERS)

        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            recovery_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Проверяем наличие ссылки 'Восстановление пароля'"):
            assert recovery_page.check_is_displayed(Rl.LINK_RESET_PASSWORD), \
                f"Искали на странице {driver.current_url} элемент {Rl.LINK_RESET_PASSWORD}, не нашли"

        with allure.step("Нажимаем на ссылку 'Восстановление пароля'"):
            recovery_page.click_element(Rl.LINK_RESET_PASSWORD)

        with allure.step("Проверяем наличие кнопки 'Восстановить'"):
            assert recovery_page.check_is_displayed(Rl.BUTTON_RECOVER), \
                f"Кнопка 'Восстановить' не найдена на странице {driver.current_url}"

    @allure.title('Ввод email и нажатие кнопки "Восстановить"')
    @allure.description('Вводим email и проверяем отображение поля для ввода кода из письма')
    def test_set_email_and_click_button_recover(self, driver, create_data_fake_user):
        data_user = create_data_fake_user

        with allure.step("Открываем страницу магазина"):
            recovery_page = AuthPage(driver)
            recovery_page.open(Bd.URL_STELLAR_BURGERS)

        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            recovery_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Переходим на страницу восстановления пароля"):
            recovery_page.click_element(Rl.LINK_RESET_PASSWORD)

        with allure.step("Вводим email в поле для восстановления пароля"):
            recovery_page.set_input(Rl.INPUT_EMAIL_RESET, data_user.get("email"))

        with allure.step("Нажимаем кнопку 'Восстановить'"):
            recovery_page.click_element(Rl.BUTTON_RECOVER)

        with allure.step("Проверяем отображение поля для ввода кода из письма"):
            assert recovery_page.check_is_displayed(Rl.INPUT_COD_FROM_MAIL), \
                f"Поле для ввода кода из письма не найдено на странице {driver.current_url}"

    @allure.title('Проверка активности поля ввода пароля после нажатия на иконку')
    @allure.description('Проверяем, что поле ввода пароля становится активным после нажатия на иконку')
    def test_click_icon_set_input_active_status(self, driver, create_data_fake_user):
        data_user = create_data_fake_user

        with allure.step("Открываем страницу магазина"):
            recovery_page = AuthPage(driver)
            recovery_page.open(Bd.URL_STELLAR_BURGERS)

        with allure.step("Нажимаем на кнопку 'Личный кабинет'"):
            recovery_page.click_element(Hl.BUTTON_PERSONAL_ACCOUNT)

        with allure.step("Переходим на страницу восстановления пароля"):
            recovery_page.click_element(Rl.LINK_RESET_PASSWORD)

        with allure.step("Вводим email в поле для восстановления пароля"):
            recovery_page.set_input(Rl.INPUT_EMAIL_RESET, data_user.get("email"))

        with allure.step("Нажимаем кнопку 'Восстановить'"):
            recovery_page.click_element(Rl.BUTTON_RECOVER)

        with allure.step("Нажимаем на иконку отображения пароля"):
            recovery_page.click_element(Rl.ICON_SHOW)

        with allure.step("Проверяем, что поле ввода пароля стало активным"):
            input_password = recovery_page.find_element(Rl.INPUT_PASSWORD)
            assert "input_status_active" in input_password.get_attribute("class"), \
                "Поле ввода пароля не стало активным после нажатия на иконку"