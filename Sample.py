import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stage.us-east-2.admin.revdoc.link/dashboard/user/users/new")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID, 'email').send_keys('rushendra@quadricit.com')
driver.find_element(By.ID, 'password').send_keys('Rushidoddoji1!')
driver.find_element(By.XPATH, "//span[text()='Log In']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='Users Mgmt.']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='+ Add New User']")
time.sleep(2)
dropdown_data = driver.find_element(By.XPATH, "(//input[@class='ant-select-selection-search-input")
#for i in range(len(dropdown_data)):
for i in dropdown_data:
    i.get
    print(dropdown_data[i].text)
# driver.find_element(By.XPATH, "//div[@class='select-box']").getText





