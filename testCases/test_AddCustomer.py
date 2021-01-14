import pytest
import string
import random
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from pageObjects.AddCustomerPage import AddCustomer


class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getpasswordL()
    logger = logGen.loggen()


    @pytest.mark.sanity
    def test_AddCustomer(self, setup):
        self.logger.info("******** Test_003_AddCustomer *********")
        self.logger.info("****************** Verifying Adding New Customer **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window
        self.obj_log = Login(self.driver)
        self.obj_log.setUsername(self.username)
        self.obj_log.setpassword(self.password)
        self.obj_log.loginbutton()
        self.logger.info("************* Login succesful **********")
        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("******* Adding New Customer *******")

        self.email = random_generator() + '@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Sai")
        self.addcust.setLastName("Kiran")
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        if 'customer has been added successfully.' in self.msg:
            self.logger.info("********* Add customer Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False
        self.obj_log.clickLogout()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
