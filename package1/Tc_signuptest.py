'''
Created on Aug 24, 2019

@author: Saran
'''
import unittest

class signuptest(unittest.TestCase):
    
    def test_loginbybyemail(self):
        print("this is through email")
        self.assertTrue(True)
        
    def test_loginbyfacebook(self):
        print("this is through facebook")
        self.assertTrue(True)
        
    def test_loginbytwitter(self):
        print("this is through twitter")
        self.assertTrue(True)
        
if __name__=="__main__":
    unittest.main()