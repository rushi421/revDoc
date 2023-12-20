import time

import pytest

from Utilities.readProperties import ReadCofig
from Utilities.customLogger import LogInfoGenerator
from pageObjects.LoginRev import Login
from pageObjects.AddCategory import Category
from pageObjects.AddNewSupply import Supply


class Test_003_NewSupplies:
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

        self.SupplyNew = Supply(self.driver)
        self.SupplyNew.ClickOnSupplies()
        time.sleep(2)
        self.SupplyNew.ClickOnAddNewSupply()
        self.SupplyNew.EnterSupplyID('6765642')
        self.SupplyNew.EnterSupplyName('DoctorKit')
        time.sleep(5)
        self.SupplyNew.ClickVendorDropdown()
        self.SupplyNew.SelectVendorValue()
        self.SupplyNew.EnterShortDescription('to record body temperature')
        self.SupplyNew.EnterDescription('to suck up blood or secretions')
        # self.SupplyNew.UploadFile("D:\\SeleniumPython\\UploadFiles\\dockit.webp")
        self.SupplyNew.EnterPrice('100')
        self.SupplyNew.EnterAdminFee('10')
        self.SupplyNew.EnterEffectiveDate('12-01-2023')
        self.SupplyNew.EnterTermDate('12-01-2023')
        self.SupplyNew.ClickSave()
        time.sleep(4)
        self.log.info("********************Add New Category Test Case Complete************************")
