'''
Created on Aug 24, 2019

@author: Saran
'''
import unittest

class paymenttest(unittest.TestCase):
    
    def test_paymentindollar(self):
        print("this is payment in dollar test")
        self.assertTrue(True)
        
    def test_paymentinrupees(self):
        print("this is payment in rupees test")
        self.assertTrue(True)
        
if __name__=="__main__":
    unittest.main