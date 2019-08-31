'''
Created on Aug 23, 2019

@author: Saran
'''
import unittest
from selenium import webdriver

class Assertionconcept(unittest.TestCase):
    
    def test_titlecheck(self):
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\Saran\\Downloads\\selenium\\driver\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        pagetitle=self.driver.title
        #assertEquals
        #self.assertEqual("Goongle", pagetitle, "page title mismatch")
        #self.assertTrue(pagetitle=="Google")
        self.assertFalse(pagetitle=="gooogle", "wromh ")
        self.driver.close()
        
    def test_titlecheck1(self):
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\Saran\\Downloads\\selenium\\driver\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        pagetitle=self.driver.title
        #assertEquals
        #self.assertNotEqual("Google123", pagetitle, "page title mismatch")
        self.assertIsNotNone(self.driver)
        self.driver.close()
    
        
if __name__=="__main__":
    unittest.main