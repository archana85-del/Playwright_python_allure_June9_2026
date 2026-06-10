from playwright.sync_api import sync_playwright,expect
import pytest

@pytest.mark.homePage
def test_validateTehVisibilityOfSearchBox(page,launchAmazon):    
    expect(page.locator("input#twotabsearchtextbox")).to_be_visible()
    