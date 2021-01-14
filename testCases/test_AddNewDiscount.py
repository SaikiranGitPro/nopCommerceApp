import pytest
import string
import time
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from pageObjects.AddNewDiscountPage import AddDiscountPage


class Test_006_AddDiscount:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getpasswordL()
    logger = logGen.loggen()

    @pytest.mark.regression
    def test_AddDiscount(self, setup):
        self.logger.info("******** Test_006_AddDiscount *********")
        self.logger.info("****************** Verifying Adding New Discount **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.obj_log = Login(self.driver)
        self.obj_log.setUsername(self.username)
        self.obj_log.setpassword(self.password)
        self.obj_log.loginbutton()

        self.logger.info("************* Login succesful **********")
        self.logger.info("******* Starting Adding New Discount **********")

        self.obj_New_Discount = AddDiscountPage(self.driver)
        self.obj_New_Discount.clickonPromotion()
        self.obj_New_Discount.clickonDiscounts()
        self.obj_New_Discount.clickonAddnewButton()
        self.obj_New_Discount.enterName('TestOnceEcommerce')
        self.obj_New_Discount.selectDiscounttype('Assigned to products')
        self.obj_New_Discount.enterDiscountAmt('10')
        self.obj_New_Discount.enterStartDate('7/05/2019')
        self.obj_New_Discount.enterEndDate('7/05/2022')
        self.obj_New_Discount.selectDiscountLimit('Unlimited')
        self.obj_New_Discount.enterMaximumDiscountQuatity('5')
        self.obj_New_Discount.enterAdminComment('Adding comment')
        self.obj_New_Discount.clickSaveButton()

        self.succesMsg = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text

        expedtedSring = 'The new discount has been added successfully.'

        if self.succesMsg.find(expedtedSring) != -1:
            self.logger.info('******* Added New Discount coupan sucessfully **********')
            self.logger.info('******* Test Case Passed  **************')
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AddDiscount_scr.png")
            assert True

        else:
            self.logger.info('******* Test Case Failed  **************')
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AddDiscount_scr.png")
            assert False

        self.obj_log.clickLogout()
        self.driver.close()
