import allure
from playwright.sync_api import expect
class loginPage:
    def __init__(self,page):
        self.emailTextBox = page.locator("#ap_email_login")
        self.submitBtn = page.locator('//input[@type="submit"]')
        self.passwordTextBox = page.locator("#ap_password")
        self.emailError = page.locator("#invalid-email-alert")

    @allure.step("Enter email ID")
    def enterEmailID(self,id):
        self.emailTextBox.fill(id)

    @allure.step("Click on Submit")
    def clickOnSubmit(self):
        self.submitBtn.click()

    @allure.step("Enter password")
    def enterPassword(self,pw):
        self.passwordTextBox.fill(pw)

    @allure.step("Validate email error")
    def validateEmailError(self):
        expect(self.emailError).to_be_visible(timeout=10000)