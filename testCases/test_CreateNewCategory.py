import random
import string
import time
import pytest
from pageObjects.LoginRev import Login
from Utilities.readProperties import ReadCofig
from Utilities.customLogger import LogInfoGenerator
from pageObjects.AddCategory import Category



class Test_002_NewCategory:

    baseURL = ReadCofig.getApplicationURL()
    username = ReadCofig.getUsername()
    password = ReadCofig.getPassword()

    log = LogInfoGenerator.logGen()

    @pytest.mark.order(3)
    def test_AddCategory(self, setUp):
        self.log.info("********************Add New Category Test Case Started************************")
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.categoryNew = Category(self.driver)
        self.categoryNew.ClickProcedureMgmt()
        self.categoryNew.ClickCategorySetup()
        self.categoryNew.ClickAddNewCategory()
        self.categoryName = random_generator()
        self.categoryNew.EnterCategoryName(self.categoryName)
        self.categoryNew.EnterEffectiveDate('2023-11-01')
        self.categoryNew.EnterTermDate('2023-12-01')
        self.categoryNew.ClickOnSave()
        time.sleep(5)
        self.driver.save_screenshot("C:\\Users\\rushe\\PycharmProjects\\revDoc\\Screenshots\\CategoryNew.png")
        self.log.info("********************Add New Category Test Case Completed************************")

def random_generator(size=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars)for x in range(size))
