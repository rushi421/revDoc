import time
import pytest
from Utilities.readProperties import ReadCofig
from Utilities.customLogger import LogInfoGenerator
from pageObjects.LoginRev import Login
from pageObjects.AddCategory import Category
from pageObjects.AddNewProcedure import Procedure

class Test_006_NewProcedure:
    baseURL = ReadCofig.getApplicationURL()
    username = ReadCofig.getUsername()
    password = ReadCofig.getPassword()

    log = LogInfoGenerator.logGen()


    @pytest.mark.order(4)
    def test_AddSupply(self, setUp):
        self.log.info("********************Add New Category Test Case Started************************")
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.categoryNew = Category(self.driver)
        self.categoryNew.ClickProcedureMgmt()

        self.procedureNew = Procedure(self.driver)
        self.procedureNew.clickProcedureSetup()
        self.procedureNew.clickOnAddNewProcedure()
        self.procedureNew.enterProcedureName('Sample Procedure Need to modify')
        self.procedureNew.clickCategoryDropdown()
        self.procedureNew.selectCategoryDropdownValue()
        self.procedureNew.enterCptCode('123')
        self.procedureNew.enterAboutTheService('sample data')
        self.procedureNew.enterProcedureSteps('sample data')
        self.procedureNew.clickSymptomDropdown()
        self.procedureNew.enterProcedureTime('12')
        self.procedureNew.selectGroupProcedure()
        self.procedureNew.enterProcedureKitId('12')
        self.procedureNew.enterPostCareInst('Sample data')
        self.procedureNew.selectOrderingDependent()
        self.procedureNew.selectEffectiveDate('12/20/2023')
        self.procedureNew.selectProviderType()
        self.procedureNew.selectDeliveryMethod()
        self.procedureNew.selectEligibility()
        self.procedureNew.enterCompetitivePrice('100')
        self.procedureNew.enterMaterialPrice('10')
        self.procedureNew.enterMaterialMarkUp('10')
        self.procedureNew.enterPharmaceuticalPrice('50')
        self.procedureNew.enterPharmaceuticalMarkUp('50')
        self.procedureNew.enterProcedurePrice('20')
        self.procedureNew.enterMemberFee('10')
        self.procedureNew.enterNonMemberFee('10')
        self.procedureNew.clickSaveButton()

