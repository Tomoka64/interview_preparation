def rreverse(s):
    if len(s) == 1:
        return s
    else:
        return rreverse(s[1:]) + s[0]

import unittest

class TestReverse(unittest.TestCase):
    def test_rev(self,solution):
        self.assertEqual(solution('hello'),'olleh')
        self.assertEqual(solution('hello world'),'dlrow olleh')
        self.assertEqual(solution('123456789'),'987654321')
        
        print('PASSED ALL TEST CASES!')
        
# Run Tests
test = TestReverse()
test.test_rev(rreverse)