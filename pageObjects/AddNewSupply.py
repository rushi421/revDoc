from selenium import webdriver
from selenium.webdriver.common.by import By


class Supply:
    link_Supplies_xpath = "//span[text()='Supplies']"
    button_addNewSupply_xpath = "//span[text()='+ Add New Supply']"
    textbox_SuppliesID_id = 'supplyId'
    textbox_SuppliesName_id = 'supplyName'
    dropdown_SVendorName_xpath = "//span[@class='ant-select-selection-search']"
    dropdown_VendorValue_xpath = "//div[text()='Henry Schein']"
    textbox_ShortDescription_id = 'shortDescription'
    textbox_Description_id = 'description'
    button_Upload_xpath = "//span[text()='Upload Image']"
    textbox_price_id = 'price'
    textbox_adminFee_id = 'adminFee'
    date_effective_id = 'effectiveDate'
    date_term_id = 'termDate'
    button_save_xpath = "//span[text()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnSupplies(self):
        self.driver.find_element(By.XPATH, self.link_Supplies_xpath).click()

    def ClickOnAddNewSupply(self):
        self.driver.find_element(By.XPATH, self.button_addNewSupply_xpath).click()

    def EnterSupplyID(self, supplyID):
        self.driver.find_element(By.ID, self.textbox_SuppliesID_id).send_keys(supplyID)

    def EnterSupplyName(self, supplyName):
        self.driver.find_element(By.ID, self.textbox_SuppliesName_id).send_keys(supplyName)

    def ClickVendorDropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_SVendorName_xpath).click()

    def SelectVendorValue(self):
        self.driver.find_element(By.XPATH, self.dropdown_VendorValue_xpath).click()

    def EnterShortDescription(self, shortDes):
        self.driver.find_element(By.ID, self.textbox_ShortDescription_id).send_keys(shortDes)

    def EnterDescription(self, Des):
        self.driver.find_element(By.ID, self.textbox_Description_id).send_keys(Des)

    def UploadFile(self):
        self.driver.find_element(By.XPATH, self.button_Upload_xpath).send_keys()

    def EnterPrice(self, price):
        self.driver.find_element(By.ID, self.textbox_price_id).send_keys(price)

    def EnterAdminFee(self, AdminFee):
        self.driver.find_element(By.ID, self.textbox_adminFee_id).send_keys(AdminFee)

    def EnterEffectiveDate(self, effectiveDate):
        self.driver.find_element(By.ID, self.date_effective_id).send_keys(effectiveDate)

    def EnterTermDate(self, termDate):
        self.driver.find_element(By.ID, self.date_term_id).send_keys(termDate)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

