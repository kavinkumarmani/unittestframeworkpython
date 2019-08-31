'''
Created on Aug 23, 2019

@author: Saran
'''
import unittest

class assertionclass(unittest.TestCase):
    
    def test_testclass(self):
        don=["python","java","ruby"]
        self.assertIn("python", don, "it is not there")
        
    def test_testclass1(self):
        don=["python","java","ruby"]
        self.assertNotIn("python ", don, "it is not there")
        
if __name__=="__main__":
    unittest.main
