from playwright.sync_api import Page, expect
import pytest

from pages.homePage import homePage
from pages.resultPage import resultsPage


@pytest.mark.results
def test_validatingCartCount(page: Page, homePageObj, resultsPageObj):

    homePageObj.enterSearchText("iphone 16")
    homePageObj.clickOnSearchBtn()
    page.wait_for_timeout(3000)
    count_beforeAdding = resultsPageObj.getCartCount()
    # page.pause()
    resultsPageObj.addAnItmeToCart("iPhone 16")
    page.wait_for_timeout(3000)
    count_AfterAdding = resultsPageObj.getCartCount()
    assert int(count_AfterAdding)>int(count_beforeAdding)



def test_validatingCartCount_1(page: Page, homePageObj, resultsPageObj):
    page.goto("https://www.amazon.in/")
    # homePageObj = homePage(page)
    # resultsPageObj = resultsPage(page)
    homePageObj.enterSearchText("iphone 16")
    homePageObj.clickOnSearchBtn()
    page.wait_for_timeout(3000)
    count_beforeAdding = resultsPageObj.getCartCount()
    resultsPageObj.addAnItmeToCart("iPhone 16")
    page.wait_for_timeout(3000)
    count_AfterAdding = resultsPageObj.getCartCount()
    assert int(count_AfterAdding)>int(count_beforeAdding)
    