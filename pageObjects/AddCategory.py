from selenium import webdriver
from selenium.webdriver.common.by import By

class Category:
    link_ProcedureMgmt_xpath = "//span[text()='Procedure Mgmt.']"
    link_CategorySetup_xpath = "//span[text()='Category Setup']"
    button_AddNewCategory_xpath = "//span[text()='+ Add New Category']"
    textbox_CategoryName_id = "procedureCategoryName"
    date_CategoryEffDate_id = "procedureCategoryEffectiveDate"
    date_CategoryTermDate_id = "procedureCategoryTermDate"
    button_CategorySave_xpath = "//span[text()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickProcedureMgmt(self):
        self.driver.find_element(By.XPATH, self.link_ProcedureMgmt_xpath).click()

    def ClickCategorySetup(self):
        self.driver.find_element(By.XPATH, self.link_CategorySetup_xpath).click()

    def ClickAddNewCategory(self):
        self.driver.find_element(By.XPATH, self.button_AddNewCategory_xpath).click()

    def EnterCategoryName(self, cname):
        self.driver.find_element(By.ID, self.textbox_CategoryName_id).send_keys(cname)

    def EnterEffectiveDate(self, eDate):
        self.driver.find_element(By.ID, self.date_CategoryEffDate_id).send_keys(eDate)

    def EnterTermDate(self, tDate):
        self.driver.find_element(By.ID, self.date_CategoryTermDate_id).send_keys(tDate)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, self.button_CategorySave_xpath).click()
