'''
Created on Aug 23, 2019

@author: Saran
'''
import unittest
from selenium import webdriver

class searchtest(unittest.TestCase):
    
    def test_google(self):
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\Saran\\Downloads\\selenium\\driver\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("title of this page: " +self.driver.title)
        
    def test_sathya(self):
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\Saran\\Downloads\\selenium\\driver\\chromedriver.exe")
        self.driver.get("https://www.sathya.in/")
        print("title of this page: " +self.driver.title)
        
if __name__=="__main__":
    unittest.main()
        