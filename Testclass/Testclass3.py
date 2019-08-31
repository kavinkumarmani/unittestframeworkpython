import unittest

from selenium import webdriver

def setupmodule(self): #will execute before class and all methods
    print("setupmodule")
    
def tearDownmodule(self):#will execute after the class
    print("teardown module")

class unittestframemethods(unittest.TestCase):
    
    @classmethod
    def setUp(self):#will execute before the testmethods
        print("sathya.in")
    
    @classmethod
    def tearDown(self):#will execute after the testmethods
        print("sathya.in logout")
        
    @classmethod
    def setUpClass(cls):#will excute once before all the methods
        print("open application")
        
    @classmethod
    def tearDownClass(cls):#will execute after all the test methods
        print("close application")
    
    def test_login(self):
        print("login check")
        
    def test_home(self):
        print("home check")
        
    def test_electronics(self):
        print("categories check")
        
    def test_laptops(self):
        print("laptops check")
        
        
if __name__=="__main__":
    unittest.main()
