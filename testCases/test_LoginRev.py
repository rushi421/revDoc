import time
import pytest
from pageObjects.LoginRev import Login
from Utilities.readProperties import ReadCofig
from Utilities.customLogger import LogInfoGenerator


class Test_001_Login:
    baseURL = ReadCofig.getApplicationURL()
    #username = ReadCofig.getUsername()
    #password = ReadCofig.getPassword()

    log = LogInfoGenerator.logGen()

    @pytest.mark.xfail
    @pytest.mark.order(1)
    def test_LoginPage(self, setUp):
        self.log.info("***************TC_001 Started*************************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(1)
        if act_title == 'React App':
            assert True
            self.log.info("***************TC_001 Completed*************************")
        else:
            self.driver.save_screenshot("C:\\Users\\rushe\\PycharmProjects\\revDoc\\Screenshots\\InvalidWebpage.png")
            assert False
            self.log.info("***************TC_001 Failed*************************")

    @pytest.mark.order(2)
    @pytest.mark.parametrize("username, password",
                             [("mani12@gmail.com", "Rushi123"),
                              ("rushendra@quadricit.com", "RushiDoddoji1!"),
                              ("gepev70370@lanxi8.com", "Rushi123")])
    def test_LoginRevDoc(self, setUp, username, password):
        self.log.info("***************TC_001 Started*************************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == 'React App':
            assert True
            self.log.info("***************TC_001 Completed*************************")
        else:
            self.driver.save_screenshot("C:\\Users\\rushe\\PycharmProjects\\revDoc\\Screenshots\\InvalidWebpage.png")
            assert False
