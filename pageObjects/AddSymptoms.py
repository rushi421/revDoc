from selenium.webdriver.common.by import By

class symptoms:
    link_symptoms_xpath = "(//span[text()='Symptoms'])[1]"
    link_symptoms2_xpath = "(//span[text()='Symptoms'])[2]"
    button_addSymptoms_xpath = "//span[text()='+ Add New Symptom']"
    textbox_SymptomName_id = 'symptomName'
    dropdown_category_xpath = "//span[text()='Category Name']"
    textbox_newCategory_xpath = "(//input[@type='text'])[2]"
    button_addNew_xpath = "//span[text()='Add New']"
    #dropdown_categoryVale_xpath = "//div[text()='Hematologic/Lymphatic']"
    button_save_xpath = "//span[text()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def clickSymptomLink(self):
        self.driver.find_element(By.XPATH, self.link_symptoms_xpath).click()

    def clickSymptom2Link(self):
        self.driver.find_element(By.XPATH, self.link_symptoms2_xpath).click()

    def clickAddSymptomButton(self):
        self.driver.find_element(By.XPATH, self.button_addSymptoms_xpath).click()

    def enterSymptomName(self, symptomName):
        self.driver.find_element(By.ID, self.textbox_SymptomName_id).send_keys(symptomName)

    def clickCategory(self):
        self.driver.find_element(By.XPATH, self.dropdown_category_xpath).click()

    def textToCreateNewCategory(self, newCat):
        self.driver.find_element(By.XPATH, self.textbox_newCategory_xpath).send_keys(newCat)

    def clickAddNewButton(self):
        self.driver.find_element(By.XPATH, self.button_addNew_xpath).click()

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()