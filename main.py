from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.get('https://admin-demo.nopcommerce.com/')
driver.maximize_window()
driver.find_element_by_xpath("//input[@class='button-1 login-button'][@value='Log in']").click()
time.sleep(4)
driver.find_element_by_xpath("//span[contains(text(),'Promotions')]").click()
driver.find_element_by_xpath("//span[@class='menu-item-title'][contains(text(),'Discounts')]").click()
driver.find_element_by_xpath("//a[@class='btn bg-blue']").click()
driver.find_element_by_id("Name").send_keys('Thomas')
drp=Select(driver.find_element_by_id("DiscountTypeId"))
drp.select_by_visible_text('Assigned to products')

driver.find_element_by_xpath("//*[@id='pnlDiscountAmount']/div[2]/span[1]/span/input[1]").send_keys('10')

driver.find_element_by_id("StartDateUtc").send_keys("7/05/2001")
driver.find_element_by_id("EndDateUtc").send_keys("7/09/2020")
#driver.find_element_by_id("DiscountLimitationId").click()
driver.find_element_by_xpath("//*[@id='pnlMaximumDiscountedQuantity']/div[2]/span[1]/span/input[1]").send_keys("10")
driver.find_element_by_id("AdminComment").send_keys("Adding Discount")
driver.find_element_by_xpath("//button[@name='save']").click()
time.sleep(2)
text_msg=driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text
print(text_msg)



#driver.find_element_by_xpath("//a[@href='#']//span[contains(text(),'Customers')]").click()
#driver.find_element_by_xpath("//span[@class='menu-item-title'][contains(text(),'Customers')]").click()
#driver.find_element_by_id("SearchEmail").send_keys("saikiran2316@gmail.com")
#driver.find_element_by_id("search-customers").click()
#print(len(driver.find_elements_by_xpath("//table[@id='customers-grid']//tbody/tr")))
#print(len(driver.find_elements_by_xpath("//table[@id='customers-grid']//tbody/tr/td")))