from selenium import webdriver
from selenium.webdriver.common.by import By


class AtHomeLabs:
    link_atHomeLabsSetUp_xpath = "//span[text()='At Home Labs Set Up']"
    button_addNewAtHomeLab_xpath = "//span[text()='+ Add New At Home Lab']"
    textbox_supplyID_id = 'vendorLabId'
    dropdown_typeOfTest_xpath = "(//div[@class='ant-select-selector'])[1]"
    dropdownValue_typeofTest_xpath = "(//div[text()='Self Administered'])[2]"
    dropdown_labVendorName_xpath = "(//div[@class='ant-select-selector'])[2]"
    dropdownValue_labVendorName_xpath = "(//div[text()='imaware'])[2]"
    textbox_atHomeLabName_id = 'labName'
    textbox_brandName_id = 'brandName'
    description_whatsNext_id = 'whatsNextText'
    description_procedureSteps_id = 'procedureStepsText'
    description_PostCareInstructions_id = 'postCareText'
    description_description_id = 'description'
    #date_atHomeLabEffective_id = 'effectiveDate'
    #date_atHomeLabTerm_id = 'termDate'
    button_addBiomarkers_xpath = "//span[text()='Add Biomarkers']"
    checkbox_selectBiomarker_xpath = "(//input[@class='ant-checkbox-input'])[2]"
    button_addBiomarkersPopUP_xpath = "(//span[text()='Add Biomarkers'])[2]"
    checkbox_eligibility_xpath = "//input[@class='ant-checkbox-input']"
    textbox_atHomeLabPrice_id = 'labPrice'
    textbox_memberAppFee_id = 'plusMembershipAppFee'
    textbox_nonMemberAppFee_id = 'basicMembershipAppFee'
    button_save_xpath = "//span[text()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def clickAtHomeLabLink(self):
        self.driver.find_element(By.XPATH, self.link_atHomeLabsSetUp_xpath).click()

    def clickAddNewHomeLab(self):
        self.driver.find_element(By.XPATH, self.button_addNewAtHomeLab_xpath).click()

    def enterSupplyID(self, supplyID):
        self.driver.find_element(By.ID, self.textbox_supplyID_id).send_keys(supplyID)

    def clickOnTypeOfTestDropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_typeOfTest_xpath).click()

    def selectTypeOfTestDrpValue(self):
        self.driver.find_element(By.XPATH, self.dropdownValue_typeofTest_xpath).click()

    def clickOnLabVendorDrpdwn(self):
        self.driver.find_element(By.XPATH, self.dropdown_labVendorName_xpath).click()

    def selectLabVendorValue(self):
        self.driver.find_element(By.XPATH, self.dropdownValue_labVendorName_xpath).click()

    def enterLabName(self, labName):
        self.driver.find_element(By.ID, self.textbox_atHomeLabName_id).send_keys(labName)

    def enterBrandName(self, brandName):
        self.driver.find_element(By.ID, self.textbox_brandName_id).send_keys(brandName)

    def enterWhatsNext(self, whatsNextDes):
        self.driver.find_element(By.ID, self.description_whatsNext_id).send_keys(whatsNextDes)

    def enterProcedureSteps(self, procedureSteps):
        self.driver.find_element(By.ID, self.description_procedureSteps_id).send_keys(procedureSteps)

    def enterPostCareInstructions(self, postCareInstruction):
        self.driver.find_element(By.ID, self.description_PostCareInstructions_id).send_keys(postCareInstruction)

    def enterDescription(self, description):
        self.driver.find_element(By.ID, self.description_description_id).send_keys(description)

    def clickAddBiomarkers(self):
        self.driver.find_element(By.XPATH, self.button_addBiomarkers_xpath).click()

    def selectBiomarker(self):
        self.driver.find_element(By.XPATH, self.checkbox_selectBiomarker_xpath).click()

    def clickBioMarkerOnPopup(self):
        self.driver.find_element(By.XPATH, self.button_addBiomarkersPopUP_xpath).click()

    def enterLabPrice(self, labPrice):
        self.driver.find_element(By.ID, self.textbox_atHomeLabPrice_id).send_keys(labPrice)

    def enterMemberFee(self, memberFee):
        self.driver.find_element(By.ID, self.textbox_memberAppFee_id).send_keys(memberFee)

    def enterNonMemberFee(self, nonMemberFee):
        self.driver.find_element(By.ID, self.textbox_nonMemberAppFee_id).send_keys(nonMemberFee)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()
