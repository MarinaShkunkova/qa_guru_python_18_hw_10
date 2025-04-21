import allure
from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "shkunkova")
@allure.feature("Декораторы")
@allure.story("Использование декораторов")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-integration-example")
    go_to_repository("eroshenkoam/allure-integration-example")
    open_issues_tab()
    should_see_text("No result")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")
    browser.driver.fullscreen_window()


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issues_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие текста {text}")
def should_see_text(text):
    s(by.text("No results")).should(be.visible)
