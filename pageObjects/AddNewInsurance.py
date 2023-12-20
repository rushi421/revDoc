from selenium.webdriver.common.by import By

class AddInsurance:
    textbox_insuranceOrganization_id = 'company'
    textbox_insurancePlan_id = 'plans_0_planName'
    date_insuranceEffectiveDate_id = 'plans_0_effectiveDate'
    date_insuranceTermDate_id = 'plans_0_termDate'

    def __init__(self, driver):
        self.driver = driver

    def EnterInsuranceOrganization(self, ION):
        self.driver.find_element(By.ID, self.textbox_insuranceOrganization_id).send_keys(ION)

    def EnterInsurancePlan(self, plan):
        self.driver.find_element(By.ID, self.textbox_insurancePlan_id).send_keys(plan)

    def EnterInsuranceEffectiveDate(self,eDate):
        self.driver.find_element(By.ID, self.date_insuranceEffectiveDate_id).send_keys(eDate)

    def EnterInsuranceTermDate(self, tDate):
        self.driver.find_element(By.ID, self.date_insuranceTermDate_id).send_keys(tDate)
