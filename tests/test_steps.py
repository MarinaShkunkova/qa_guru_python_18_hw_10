import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Allure.step")
    allure.dynamic.story("With allure.step")
    allure.dynamic.link("https://github.com", name="Testing")

    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
        browser.driver.fullscreen_window()

    with allure.step("Ищем репозиторий"):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').send_keys("eroshenkoam/allure-integration-example").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-integration-example")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие текста 'No results'"):
        s(by.text("No results")).should(be.visible)
