import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import BaseData as Bd
from selenium.webdriver.common.action_chains import ActionChains



class BasePage: #Класс с базовыми методами

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Bd.TIMEOUT)

    # Открыть браузер
    @allure.step('Открываем страницу {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Ищем элементы по {locator} и возвращением список элементов')
    def find_elements(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    @allure.step('Ищем элемент по {locator} и возвращением его')
    def find_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    # Метод ждущий загрузки элемента по локатору
    @allure.step('Ждем когда элемент {locator} загрузится')
    def wait_for_load(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за отведенное время.")
            raise

    # Метод ждущий по локатору когда элемент станет кликабельным
    @allure.step('Ждем когда элемент {locator} станет кликабельным')
    def wait_for_click(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не стал кликабельным за отведенное время.")
            raise


    # Метод скроллит страницу к элементу
    @allure.step('Скроллит страницу к {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_load(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    # Метод проверяющий видимость элемента на странице, возвращает True если элемент отображается
    @allure.step('Проверяем видимость элемента {locator}')
    def check_is_displayed(self, locator):
        try:
            self.wait_for_load(locator)
            is_displayed = self.driver.find_element(*locator).is_displayed()
            return is_displayed
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент с локатором {locator} не найден на странице.")

    # Метод нажимающий на элемент
    @allure.step('Нажимаем на элемент {locator}')
    def click_element(self, locator):
        try:
            self.wait_for_click(locator)
            time.sleep(1)
            self.driver.find_element(*locator).click()
        except Exception as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e

    # Метод нажимающий на элемент
    @allure.step('Нажимаем JS на элемент {locator}')
    def click_element_js(self, locator):
        try:
            button = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", button)
        except Exception as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e

    # Метод для ввода текста, set_data - текст для ввода
    @allure.step('Вводим текст {set_data} в поле ввода {locator}')
    def set_input(self, locator, set_data):
        self.wait_for_click(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(set_data)

    # Метод сравнивает Ожидаем URL(expect_url) c Фактическим URL(actual_url), если совпадает возвращает True
    # Метод так же принимает Локатор, для ожидания загрузки страницы
    @allure.step('Сравниваем URL текущей страницы с ожидаемой {expect_url}')
    def check_current_url(self, expect_url, locator=None):
        if locator:
            self.wait_for_load(locator)
        actual_url = self.driver.current_url
        if actual_url != expect_url:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Ожидаемый URL: {expect_url}, Фактический URL: {actual_url}")
        return True

    @allure.step('Переключаемся на вкладку {number_tab}')
    def switch_tab(self, number_tab):
        if number_tab < 1 or number_tab > len(self.driver.window_handles):
            raise ValueError(f"Вкладка с номером {number_tab} не существует.")
        self.driver.switch_to.window(self.driver.window_handles[number_tab - 1])

    @allure.step('Проверяем видимость элемента')
    def check_element_is_focused(self, locator):
        element = self.driver.find_element(*locator)
        is_focused = self.driver.execute_script("return document.activeElement === arguments[0];", element)
        return is_focused

    @allure.step('Ожидаем исчезновение элемента {locator}')
    def invis_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Перетаскиваем элемент {locator_element} в зону {locator_where} ')
    def drag_and_drop(self, locator_element, locator_where):
        element = self.find_elements(locator_element)
        section = self.find_element(locator_where)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element[0], section).perform()

    @allure.step('Перетаскиваем элемент {locator_element} в зону {locator_where} ')
    def drag_and_drop_js(self, locator_element, locator_where):
        element = self.find_elements(locator_element)
        section = self.find_element(locator_where)

        # JavaScript для перетаскивания
        self.driver.execute_script(
            "function createEvent(typeOfEvent) { " +
            "var event = document.createEvent('CustomEvent'); " +
            "event.initCustomEvent(typeOfEvent, true, true, null); " +
            "event.dataTransfer = { " +
            "data: {}, " +
            "setData: function(key, value) { this.data[key] = value; }, " +
            "getData: function(key) { return this.data[key]; } " +
            "}; " +
            "return event; " +
            "} " +
            "function dispatchEvent(element, typeOfEvent, event) { " +
            "if (element.dispatchEvent) { " +
            "element.dispatchEvent(event); " +
            "} else if (element.fireEvent) { " +
            "element.fireEvent('on' + typeOfEvent, event); " +
            "} " +
            "} " +
            "function simulateHTML5DragAndDrop(element, destination) { " +
            "var dragStartEvent = createEvent('dragstart'); " +
            "dispatchEvent(element, 'dragstart', dragStartEvent); " +
            "var dropEvent = createEvent('drop'); " +
            "dispatchEvent(destination, 'drop', dropEvent); " +
            "var dragEndEvent = createEvent('dragend'); " +
            "dispatchEvent(element, 'dragend', dragEndEvent); " +
            "} " +
            "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
            element[0],
            section
        )
