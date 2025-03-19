from selenium.webdriver.common.by import By



class OrderHistoryLocators:
    CARD_ORDER = (By.XPATH, "//li[contains(@class,'OrderHistory_list')]")
    MODAL_ORDER = (By.XPATH, "//div[contains(@class,'Modal_orderBox')]")
    NUMBER_ORDER = (By.XPATH, "//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]")
    COUNT_ORDERS_ALL_TIME = (By.XPATH, "//div[contains(@class,'undefined')]/p[contains(@class,'text_type_digits-large')]")
    # Локатор для числа "Выполнено за сегодня"
    COUNT_ORDERS_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
