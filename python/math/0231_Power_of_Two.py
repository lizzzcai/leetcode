'''
22/02/2020

231. Power of Two - Easy

Tag: Math, Bit Manipulation

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false


'''

# Solution
class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        
        return n == 1
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for func in [Solution1().isPowerOfTwo]:

            self.assertEqual(func(0), False)
            self.assertEqual(func(1), True)
            self.assertEqual(func(2), True)
            self.assertEqual(func(16), True)
            self.assertEqual(func(218), False)

if __name__ == '__main__':
    unittest.main()