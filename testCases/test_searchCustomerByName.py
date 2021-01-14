import pytest
import time
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from pageObjects.SearchCustomerPage import SearchCustomer


class Test_005_SearchCustomerByName:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getpasswordL()
    logger=logGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("****************** Test_005_SearchCustomerByName **********************")
        self.logger.info("****************** Verifying Home Page Tittle **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window

        self.obj_log = Login(self.driver)
        self.obj_log.setUsername(self.username)
        self.obj_log.setpassword(self.password)
        self.obj_log.loginbutton()
        self.logger.info("************* Login succesful **********")
        self.logger.info("******* Starting Search Customer By Email **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.logger.info("************* searching customer by emailID **********")

        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(4)
        status = searchcust.searchCustomerByName("Victoria Terces")
        self.driver.quit
        assert True == status
        self.logger.info("***************  Test_005_SearchCustomerByName Finished  *********** ")