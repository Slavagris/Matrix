from allure import step, suite, story, severity, description, feature
from pages.base_page import BasePage
from locators.matix_page_locators import *
from playwright.sync_api import Page


def test_goto_vk(page: Page):
    with step("Войти на страницу"):
        base = BasePage(page)
        base.open()
    with step("Проверить перреходы по иконкам соцесетей"):
        with step("Перейти на страницу VK"):
            base.click_by_locator(LOCATOR_ICON_VK)


def test_goto_telegram(page: Page):
    with step("Войти на страницу"):
        base = BasePage(page)
        base.open()
    with step("Проверить перреходы по иконкам соцесетей"):
        with step("Перейти на страницу Telegram"):
            base.click_by_locator(LOCATOR_ICON_TELEGRAM)


def test_goto_instagramm(page: Page):
    with step("Войти на страницу"):
        base = BasePage(page)
        base.open()
    with step("Проверить перреходы по иконкам соцесетей"):
        with step("Перейти на страницу Instagram"):
            base.click_by_locator(LOCATOR_ICON_INSTAGRAM)


def test_get_matrix(page: Page):
    with step("Войти на страницу"):
        base = BasePage(page)
        base.open()
    with step("Заполнить поле Дата Рождения"):
        base.click_by_placeholder("01.01.1901").fill("2000-02-02")
    with step("Нажать на кнопку 'Узнать'"):
        base.click_by_locator(LOCATOR_BTN_DISCOVER)











