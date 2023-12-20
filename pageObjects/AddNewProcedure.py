from selenium.webdriver.common.by import By


class Procedure:
    linkText_procedureSetUp_xpath = "//span[text()='Procedure Setup']"
    button_addNewProcedure_xpath = "//span[text()='+ Add New Procedure']"
    textbox_procedureName_id = 'procedureName'
    dropDown_category_xpath = "//span[text()='Category Name']"
    dropDownValue_selectCategory_xpath = "(//div[@class='ant-select-item-option-content'])[1]"
    textbox_cptCode_id = 'cptCode'
    textbox_aboutService_id = 'aboutText'
    textbox_procedureSteps_id = 'procedureStepsText'
    dropDown_symptoms_xpath = "//span[text()='Select Symptoms']"
    textbox_procedureTime_id = 'procedureTime'
    radioButtonNO_groupProcedure_xpath = "(//span[text()='No'])[1]"
    radioButtonYES_groupProcedure_xpath = "(//span[text()='Yes'])[1]"
    textbox_PTPAP_id = 'procedureTimePerPerson'
    textbox_procedureKitId_id = 'procedureKitIds'
    textbox_postCareInstructions_id = 'postCareInstructionsText'
    radioButtonYES_orderingDependent_xpath = "(//span[text()='Yes'])[2]"
    radioButtonNO_orderingDependent_xpath = "(//span[text()='No'])[2]"
    date_procedureEffectiveDate_id = 'procedureEffectiveDate'
    date_procedureTermDate_id = 'procedureTermDate'
    checkbox_providerType_xpath = "//span[text()='Medical Doctor (MD)/Osteopathic Doctor (DO)']"
    checkbox_deliveryMethod_xpath = "//span[text()='Facility']"
    radioButtonYES_eligibility_xpath = "(//span[text()='Yes'])[3]"
    radioButtonNO_eligibility_xpath = "(//span[text()='No'])[3]"
    textbox_competitivePrice_id = 'competitivePrice'
    textbox_materialPrice_id = 'materialPrice'
    textbox_materialMarkup_id = 'materialMarkup'
    textbox_procedurePrice_id = 'procedurePrice'
    textbox_memberAppFee_id = 'memberAppFee'
    textbox_nonMemberAppFee_id = 'nonMemberAppFee'
    button_save_xpath = "//span[text()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def clickProcedureSetup(self):
        self.driver.find_element(By.XPATH, self.linkText_procedureSetUp_xpath).click()

    def clickOnAddNewProcedure(self):
        self.driver.find_element(By.XPATH, self.button_addNewProcedure_xpath).click()

    def enterProcedureName(self, procedureName):
        self.driver.find_element(By.ID, self.textbox_procedureName_id).send_keys(procedureName)

    def clickCategoryDropdown(self):
        self.driver.find_element(By.XPATH, self.dropDown_category_xpath).click()

    def selectCategoryDropdownValue(self):
        self.driver.find_element(By.XPATH, self.dropDownValue_selectCategory_xpath).click()

    def enterCptCode(self, cptCode):
        self.driver.find_element(By.ID, self.textbox_cptCode_id).send_keys(cptCode)

    def enterAboutTheService(self, aboutService):
        self.driver.find_element(By.ID, self.textbox_aboutService_id).send_keys(aboutService)

    def enterProcedureSteps(self, procedureSteps):
        self.driver.find_element(By.ID, self.textbox_procedureSteps_id).send_keys(procedureSteps)

    def clickSymptomDropdown(self):
        self.driver.find_element(By.XPATH, self.dropDown_symptoms_xpath).click()

    def enterProcedureTime(self, pTime):
        self.driver.find_element(By.XPATH, self.textbox_procedureTime_id).send_keys(pTime)

    def selectGroupProcedure(self):
        self.driver.find_element(By.XPATH, self.radioButtonNO_groupProcedure_xpath).click()

    def enterProcedureKitId(self, pKitID):
        self.driver.find_element(By.ID, self.textbox_procedureKitId_id).send_keys(pKitID)

    def enterPostCareInst(self, PCI):
        self.driver.find_element(By.ID, self.textbox_postCareInstructions_id).send_keys(PCI)

    def selectOrderingDependent(self):
        self.driver.find_element(By.XPATH, self.radioButtonNO_orderingDependent_xpath).click()

    def 