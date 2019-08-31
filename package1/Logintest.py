'''
Created on Aug 24, 2019

@author: Saran
'''
import unittest

class logintest(unittest.TestCase):
    
    def test_signupbyemail(self):
        print("this is through email")
        self.assertTrue(True)
        
    def test_signupbyfacebook(self):
        print("this is through facebook")
        self.assertTrue(True)
        
    def test_signupbytwitter(self):
        print("this is through twitter")
        self.assertTrue(True)
        
if __name__=="__main__":
    unittest.main()