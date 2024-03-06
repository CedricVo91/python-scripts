import unittest
import function_tobetested as function_test

class TestFunction(unittest.TestCase):
    def test_function(self):
        input = "1"
        result = function_test(self,input)


if __name__ == "main":
    unittest.main()



