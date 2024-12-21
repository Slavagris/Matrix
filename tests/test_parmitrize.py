import pytest
from allure import step
from pages.base_page import BasePage
from locators.matix_page_locators import *
from playwright.sync_api import Page

# Параметры для тестов переходов по иконкам соцсетей
social_networks = [
    ("VK", LOCATOR_ICON_VK),
    ("Telegram", LOCATOR_ICON_TELEGRAM),
    ("Instagram", LOCATOR_ICON_INSTAGRAM)
]

@pytest.mark.parametrize("social_name, locator", social_networks)
def test_goto_social_network(page: Page, social_name: str, locator: str):
    with step("Войти на страницу"):
        base = BasePage(page)
        base.open()
    with step(f"Проверить переход на страницу {social_name}"):
        base.click_by_locator(locator)

# Параметры для тестов заполнения даты рождения
date_tests = [
    ("2000-02-02", "01.01.1901"),
    ("", "01.01.1901")  # Тест на ошибку
]

@pytest.mark.parametrize("date_value, placeholder", date_tests)
def test_get_matrix(page: Page, date_value: str, placeholder: str):
    with step("Войти на страницу"):
        base = BasePage(page)
        base.open()
    with step("Заполнить поле Дата Рождения"):
        if date_value:
            base.click_by_placeholder(placeholder).fill(date_value)
        else:
            base.click_by_placeholder(placeholder).fill("")  # Оставляем поле пустым для теста ошибки
    with step("Нажать на кнопку 'Узнать'"):
        base.click_by_locator(LOCATOR_BTN_DISCOVER)

    if not date_value:  # Проверка на ошибку, если дата не заполнена
        with step("Получить сообщение с ошибкой 'Заполните поле даты'"):
            base.get_by_placeholder("Заполните поле даты")
