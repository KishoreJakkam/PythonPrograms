'''
Created on Oct 15, 2017

@author: kishore
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class LoginTest(unittest.TestCase):
    def setUp(self):
        #self.driver=webdriver.Firefox(executable_path="D:\\Kishore_IMP\\Softwares\soft\\Selenium_Vam\\Selenium\\geckodriver.exe");
        self.driver = webdriver.Chrome("D:\\Kishore_IMP\\Softwares\\soft\\Selenium_Vam\\Selenium\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")

    def test_Login(self):
        driver=self.driver
        FacebookUsername="kishore_262001@yahoo.co.in"
        FacebookPass="Twinkle@2k7938106"
        emailFieldID="email"
        passFieldID="pass"
        LoginButtonXpath="//input[@value='Log In']"
        fbLogoXpath="(//a[contains(@href,'Logo')])[1]"

        emailFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passFieldID ))
        #loginFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(LoginButtonXpath))

        #emailFieldElement=self.driver.find_element_by_id(emailFieldID)
        #passFieldElement=self.driver.find_element_by_id(passFieldID)
        loginFieldElement=self.driver.find_element_by_xpath(LoginButtonXpath)

        emailFieldElement.clear()
        emailFieldElement.send_keys(FacebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(FacebookPass)
        loginFieldElement.click()


        #WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(fbLogoXpath))

    def test_youtube(self):
        driver=self.driver
        self.driver.maximize_window()
        self.driver.get("https://www.youtube.com/")

    def tearDown(self):
       self.driver.quit()
       

       if __name__ == "__main__":
         unittest.main()



