import random
import string
import time

import pytest

from pageObjects.LoginRev import Login
from pageObjects.AddSymptoms import symptoms
from Utilities.readProperties import ReadCofig
from Utilities.customLogger import LogInfoGenerator
from pageObjects.AddNewSupply import Supply


class Test_004_NewSymptom:
    baseURL = ReadCofig.getApplicationURL()
    username = ReadCofig.getUsername()
    password = ReadCofig.getPassword()

    log = LogInfoGenerator.logGen()

    @pytest.mark.order(6)
    def test_AddNewSymptom(self, setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.NewSymptom = symptoms(self.driver)
        self.NewSymptom.clickSymptomLink()
        self.NewSymptom.clickSymptom2Link()
        time.sleep(2)
        self.NewSymptom.clickAddSymptomButton()
        self.newSymptom = random_generator()
        self.NewSymptom.enterSymptomName(self.newSymptom)

        self.SupplyNew = Supply(self.driver)
        self.SupplyNew.EnterEffectiveDate('2023-11-01')
        self.SupplyNew.EnterTermDate('2023-12-01')
        time.sleep(2)
        """self.NewSymptom.clickCategory()
        self.NewSymptom.textToCreateNewCategory('Dengue')
        self.NewSymptom.clickAddNewButton()"""
        self.NewSymptom.clickOnSave()
        time.sleep(5)

def random_generator(size=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars)for x in range(size))

