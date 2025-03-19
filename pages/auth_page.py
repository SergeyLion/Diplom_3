import allure
from pages.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryLocators as Rl



class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Авторизуемся в магазин')
    def auth_login(self, user_email, user_password):
        self.set_input(Rl.INPUT_USERNAME, user_email)
        self.set_input(Rl.INPUT_AUTH_PASSWORD, user_password)
        self.click_element(Rl.BUTTON_ENTER)

