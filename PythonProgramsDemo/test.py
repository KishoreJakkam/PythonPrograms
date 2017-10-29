'''
Created on Oct 15, 2017

@author: kishore
'''
print("Hello Python World,Yahooooooo")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("D:\\Kishore_IMP\\Softwares\\soft\\Selenium_Vam\\Selenium\\chromedriver.exe");
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys("user")
elem = driver.find_element_by_id("pass")
elem.send_keys("pwd")
elem.send_keys(Keys.RETURN)
#driver.close()