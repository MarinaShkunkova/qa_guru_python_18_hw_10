from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_clear_selene():
    browser.open("https://github.com")
    browser.driver.fullscreen_window()
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys("eroshenkoam/allure-integration-example").press_enter()
    browser.element(by.link_text("eroshenkoam/allure-integration-example")).click()
    browser.element("#issues-tab").click()
    s(by.text("No results")).should(be.visible)
