import allure
from playwright.sync_api import sync_playwright
import pytest

from pages.homePage import homePage
from pages.loginPage import loginPage


@pytest.fixture(scope="session")
def precondition4():
    print("launching amazon")
    yield
    print("closing amazon")



@pytest.fixture(scope="function")
def precondition2():
    print("amazon2")
    yield
    print("amazon2 closing")

@pytest.fixture(scope="function")
def launchAmazon(page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(3000)
    continue_btn = page.locator("//*[contains(text(),'ontinue s')]").last

    if continue_btn.is_visible(timeout=15000):
        continue_btn.click()

@pytest.fixture(scope="function")
def homePageObj(page):
    homePageObj = homePage(page)
    return homePageObj

@pytest.fixture(scope="function")
def loginPageObj(page):
    loginPageObj = loginPage(page)
    return loginPageObj


# # @pytest.fixture(scope="function")
# @pytest.mark.parametrize("browser", ["chromium", "firefox", "safari"])
# def page(browser):
#     with sync_playwright() as p:
#         if browser == "chromium":
#             browser_instance = p.chromium.launch(headless=False)
#         elif browser == "firefox":
#             browser_instance = p.firefox.launch(headless=False)
#         else:
#             browser_instance = p.webkit.launch(headless=False)
#         context = browser_instance.new_context()
#         page = context.new_page()
#         yield page
#         browser_instance.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield   ### execute my testcase
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")

        if page:
            allure.attach(
                page.screenshot(),
                name="failed step",
                attachment_type=allure.attachment_type.PNG
            )


