from selenium import webdriver
from selenium.webdriver.support.ui import Select


class AddDiscountPage:
    link_Promotions_xpath = "//span[contains(text(),'Promotions')]"
    link_Discount_xpath = "//span[@class='menu-item-title'][contains(text(),'Discounts')]"
    btn_addnew_xpath = "//a[@class='btn bg-blue']"
    txt_name_id = "Name"
    drop_discount_id = "DiscountTypeId"
    txt_DiscountAmt_xpath = "//*[@id='pnlDiscountAmount']/div[2]/span[1]/span/input[1]"
    txt_startdate_id = "StartDateUtc"
    txt_enddate_id = "EndDateUtc"
    drop_discointLimit_id = "DiscountLimitationId"
    text_MaximumDiscountQuantity="//*[@id='pnlMaximumDiscountedQuantity']/div[2]/span[1]/span/input[1]"
    txt_Admincomment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickonPromotion(self):
        self.driver.find_element_by_xpath(self.link_Promotions_xpath).click()

    def clickonDiscounts(self):
        self.driver.find_element_by_xpath(self.link_Discount_xpath).click()

    def clickonAddnewButton(self):
        self.driver.find_element_by_xpath(self.btn_addnew_xpath).click()

    def enterName(self,value):
        self.driver.find_element_by_id(self.txt_name_id).send_keys(value)

    def selectDiscounttype(self,value):
        drp_val=Select(self.driver.find_element_by_id(self.drop_discount_id))
        drp_val.select_by_visible_text(value)

    def enterDiscountAmt(self, value):
        self.driver.find_element_by_xpath(self.txt_DiscountAmt_xpath).send_keys(value)

    def enterStartDate(self,value):
        self.driver.find_element_by_id(self.txt_startdate_id).send_keys(value)

    def enterEndDate(self,value):
        self.driver.find_element_by_id(self.txt_enddate_id).send_keys(value)

    def selectDiscountLimit(self,value):
        drp_val = Select(self.driver.find_element_by_id(self.drop_discointLimit_id))
        drp_val.select_by_visible_text(value)

    def enterMaximumDiscountQuatity(self,value):
        self.driver.find_element_by_xpath(self.text_MaximumDiscountQuantity).send_keys(value)

    def enterAdminComment(self,value):
        self.driver.find_element_by_id(self.txt_Admincomment_id).send_keys(value)

    def clickSaveButton(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()











