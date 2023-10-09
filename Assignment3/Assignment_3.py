from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.reliancedigital.in")
time.sleep(3)


cancel_button = driver.find_element("id","wzrk-cancel")
cancel_button.click()
time.sleep(2)


pincode_button =driver.find_element("xpath", "/html/body/div[1]/header/div/div/ul/li[1]/div/div/div")
pincode_button.click()
time.sleep(2)

Delivery_link =driver.find_element("id","pincode")
Delivery_link.send_keys("600053")
apply_button= driver.find_element("id","btn-apply-coupon")
apply_button.click()
time.sleep(8)






# Finding the search bar and entering text

find_bar = driver.find_element("id","suggestionBoxEle")
find_bar.send_keys("Mobile")
find_bar.send_keys(Keys.RETURN)
time.sleep(8)


# Selecting a laptop from the search results
Mobile_link = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/div/a/div/div[1]/div[2]/div/img")
Mobile_link.click()
time.sleep(5)

driver.close()

#
#
#
#
