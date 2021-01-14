from selenium import webdriver


class Login:
    textbox_Username_id = "Email"
    textbox_Password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button'][@value='Log in']"
    link_logout_linkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_Username_id).clear()
        self.driver.find_element_by_id(self.textbox_Username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_Password_id).clear()
        self.driver.find_element_by_id(self.textbox_Password_id).send_keys(password)

    def loginbutton(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linkText).click()
