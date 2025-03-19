from selenium.webdriver.common.by import By



class ConstructorLocators:
    TAB_BUN = (By.XPATH, "//div[@style='display: flex;']/div[1]")  # Таб "Булки" в конструкторе
    TAB_SAUCE = (By.XPATH, "//div[@style='display: flex;']/div[2]")  # Таб "Соусы" в конструкторе
    TAB_TOPPING = (By.XPATH, "//div[@style='display: flex;']/div[3]")  # Таб "Начинки" в конструкторе
    BURGER_INGREDIENTS = (By.XPATH, "//a[contains(@class,'BurgerIngredient')]") #Список ингредиентов
    COUNTER_NUM_INGREDIENTS = (By.XPATH, "//a[contains(@class,'BurgerIngredient')]//p[contains(@class,'counter_counter__num')]") #список счетчики ингредиентов
    HEADER_MODAL_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']") # Заголовок модального окна "Детали ингредиента"
    BUTTON_CLOSE_MODAL_INGREDIENT = (By.XPATH, "//button[contains(@class,'close_modified')]")# Кнопка "Закрыть" модального окна "Детали ингредиента"
    SECTION_ORDER = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]") # Зона сборки заказа
    BUTTON_CREATE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    BUTTON_CLOSE_MODAL_MODIFIED = (By.XPATH, "//button[contains(@class,'Modal_modal__close_modified')]") # Кнопка закрытия модального окна успеха
    NUMBER_ORDER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title_shadow')]")
    TEXT_SUCCESS_CREATE_ORDER = (By.XPATH, "//p[text()='идентификатор заказа']") # Текст "идентификатор заказа" в модальном окне успешного создания заказа
