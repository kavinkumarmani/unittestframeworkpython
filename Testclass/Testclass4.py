
import unittest

class skipconcept(unittest.TestCase):
    
    @unittest.SkipTest
    def test_skiptest(self):
        print("sample check")
        
    @unittest.skip("skipping this test")
    def test_skiptest1(self):
        print("sample1.check")
        
    @unittest.skipIf(1==1,"hai")
    def test_skiptest2(self):
        print("go to check and update")
        
    def test_skiptest3(self):
        print("helloworld")
        
    def test_skiptest4(self):
        print("sample")
        
if __name__=="__main__":
    unittest.main()
