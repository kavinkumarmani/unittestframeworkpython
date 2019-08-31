'''
Created on Aug 24, 2019

@author: Saran
'''
import unittest

from package1.Logintest import logintest
from package1.Tc_signuptest import signuptest

from package2.Tc_paymenttest import paymenttest
from package2.Tc_paymentreturns import paymentreturnstest

tc1=unittest.TestLoader().loadTestsFromTestCase(logintest)
tc2=unittest.TestLoader().loadTestsFromTestCase(signuptest)
tc3=unittest.TestLoader().loadTestsFromTestCase(paymenttest)
tc4=unittest.TestLoader().loadTestsFromTestCase(paymentreturnstest)

#creating test suites
sanitytestsuite=unittest.TestSuite([tc1,tc2])
functionaltestsuite=unittest.TestSuite([tc3,tc4])
mastersuite=unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner().run(mastersuite)
