import time
import pytest
from pageObjects.LoginRev import Login
from pageObjects.AddCategory import Category
from Utilities.readProperties import ReadCofig
from Utilities.customLogger import LogInfoGenerator
from pageObjects.AddNewAtHomeLabs import AtHomeLabs
from pageObjects.AddNewSupply import Supply


class Test_005_NewHomeLab:
    baseURL = ReadCofig.getApplicationURL()
    username = ReadCofig.getUsername()
    password = ReadCofig.getPassword()
    supplyID = ReadCofig.getSupplyID()
    labName = ReadCofig.getLabName()

    log = LogInfoGenerator.logGen()

    @pytest.mark.order(5)
    def test_addNewHomeLab(self, setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.categoryNew = Category(self.driver)
        self.categoryNew.ClickProcedureMgmt()

        self.AHL = AtHomeLabs(self.driver)
        self.AHL.clickAtHomeLabLink()
        self.AHL.clickAddNewHomeLab()
        self.AHL.enterSupplyID(self.supplyID)
        self.AHL.clickOnTypeOfTestDropdown()
        self.AHL.selectTypeOfTestDrpValue()
        self.AHL.clickOnLabVendorDrpdwn()
        self.AHL.selectLabVendorValue()
        self.AHL.enterLabName(self.labName)
        self.AHL.enterBrandName('Eurofins')
        self.AHL.enterWhatsNext('text')
        self.AHL.enterProcedureSteps('text')
        self.AHL.enterPostCareInstructions('text')
        self.AHL.enterDescription('text')
        self.SupplyNew = Supply(self.driver)
        self.SupplyNew.EnterEffectiveDate('12-01-2023')
        self.SupplyNew.EnterTermDate('12-31-2023')
        self.AHL.clickAddBiomarkers()
        self.AHL.selectBiomarker()
        self.AHL.clickBioMarkerOnPopup()
        self.AHL.enterLabPrice('150')
        self.AHL.enterMemberFee('10')
        self.AHL.enterNonMemberFee('10')
        self.AHL.clickSave()
        time.sleep(20)