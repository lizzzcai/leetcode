'''
09/05/2020

367. Valid Perfect Square - Easy

Tag: 

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

'''

from typing import List
# Solution
class Solution1:
    '''
    logn
    '''
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l+r) // 2
            x = mid * mid
            if x == num:
                return True
            elif x > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

class Solution2:
    '''
    newton
    '''
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return False
        r = num
        while r*r>num:
            r = (r + num // r) // 2
        return r*r==num

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.isPerfectSquare
            self.assertEqual(func(16), True)
            self.assertEqual(func(0), False)
            self.assertEqual(func(14), False)

if __name__ == '__main__':
    unittest.main()