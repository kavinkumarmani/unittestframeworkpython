'''
Created on Aug 25, 2019

@author: Saran
'''
from selenium import webdriver
import unittest
import HtmlTestRunner

class sathyalogintest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Users\\Saran\\Downloads\\selenium\\driver\\chromedriver.exe")
        cls.driver.maximize_window()
        
    def test_homepagetitle(self):
        self.driver.get("https://www.flipkart.com")
        self.assertNotEqual("Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books &amp; More. Best Offers!?", self.driver.title, "page title not matched")
        
    def test_logintest(self):
        self.driver.get("https://www.flipkart.com")
        #self.driver.find_element_by_xpath("//a[contains(text(),'Login & Signup')]").click()
        self.driver.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']").send_keys("7010920223")
        self.driver.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']").send_keys("Password@123")
        self.driver.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']").click()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test completed")
        
        
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))
    
