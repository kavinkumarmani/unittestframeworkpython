'''
Created on Aug 24, 2019

@author: Saran
'''
import pytest

@pytest.fixture()
def setup():
    print("setupmethod")

def testmethod(setup):
    print("this is test method1")
    
def testmethod1(setup):
    print("this is test method2")