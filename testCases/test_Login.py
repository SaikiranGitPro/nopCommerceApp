import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen


class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getpasswordL()
    logger = logGen.loggen()

    @pytest.mark.sanity
    def test_homePageTittle(self, setup):
        self.logger.info("****************** Test_001_Login **********************")
        self.logger.info("****************** Verifying Home Page Tittle **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window
        act_tittle = self.driver.title

        if act_tittle == "Your store. Login":
            self.driver.close()
            self.logger.info("****************** Home Page Tittle Test is Passed **********************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTittle.png")
            self.driver.close()
            self.logger.error("****************** Home Page Tittle Test is Failed **********************")
            assert False

    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("****************** Verifying Login Test **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window
        self.obj_log = Login(self.driver)
        self.obj_log.setUsername(self.username)
        self.obj_log.setpassword(self.password)
        self.obj_log.loginbutton()
        logTitle = self.driver.title

        if logTitle == "Dashboard / nopCommerce administration":
            self.logger.info("****************** Login Test is Passed **********************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_Login.png")
            self.driver.close()
            self.logger.error("****************** Login Test is Failed **********************")
            assert False
