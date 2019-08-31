'''
Created on Aug 24, 2019

@author: Saran
'''
import unittest

class paymentreturnstest(unittest.TestCase):
    
    def test_paymentreturnbybank(self):
        print("payment is returned")
        self.assertTrue(True)
        
if __name__=="__main__":
    unittest.main