'''
05/04/2020

258. Add Digits - Easy

Tag: Math

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

'''

from typing import List
# Solution
class Solution1:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        curr = 0
        while num:
            curr += num % 10
            num //= 10
        
        return self.addDigits(curr)
        
        
        
class Solution2:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        return 1 + (num - 1) % 9
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.addDigits
            self.assertEqual(func(38), 2)
            self.assertEqual(func(0), 0)



if __name__ == '__main__':
    unittest.main()