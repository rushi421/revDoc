from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_email_id = 'email'                           # All the web elements related to Login page.
    textbox_password_id = 'password'
    button_login_xpath = "//span[text()='Log In']"
    link_userIcon_xpath = "div[@class='iconContainer']"
    button_logout_xpath = "//li[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickOnUserIcon(self):
        self.driver.find_element(By.XPATH, self.link_userIcon_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()