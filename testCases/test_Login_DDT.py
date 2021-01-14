import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseurl = ReadConfig.getApplicationURL()
    path = ".\\TestData\\LoginTestData.xlsx"
    logger = logGen.loggen()

    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("****************** Test_002_DDT_Login **********************")
        self.logger.info("****************** Verifying Login Test **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window
        self.obj_log = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print(self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.obj_log.setUsername(self.user)
            self.obj_log.setpassword(self.password)
            self.obj_log.loginbutton()
            time.sleep(5)
            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.expected=='Pass':
                    self.logger.info("*** Passed ***")
                    self.obj_log.clickLogout()
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, 'Pass')
                elif self.expected=='Fail':
                    self.logger.info("*** Failed ***")
                    self.obj_log.clickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.expected=='Pass':
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, 'Fail')
                elif self.expected=='Fail':
                    self.logger.info('*** Passed ***')
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, 'Pass')
        if "Fail" not in lst_status:
            self.logger.info('*** Data Driven Test is Passed ***')
            self.driver.close
            assert True
        else:
            self.logger.info('*** Data Driven Test is Failed ***')
            self.driver.close
            assert False















