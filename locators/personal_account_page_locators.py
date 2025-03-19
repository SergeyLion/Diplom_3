from selenium.webdriver.common.by import By



class PersonalAccountLocators:
    TAB_PROFILER = (By.XPATH, "//a[text()='Профиль']")
    TAB_HISTORY_ORDER = (By.XPATH, "//a[text()='История заказов']")
    TAB_EXIT= (By.XPATH, "//button[text()='Выход']")
    LIST_ORDERS_HISTORY = (By.XPATH, "//ul[contains(@class,'OrderHistory_profileList')]/li") #Лист заказов пользователя
    NUMBER_ORDER = (By.XPATH, "//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]")

