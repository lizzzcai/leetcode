'''
17/07/2020

50. Pow(x, n) - Medium

Tag: Math, Binary Search

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(logn)
    Space complexity : O(1)
    '''
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1.
        
        res = 1
        while n > 1:
            if n % 2 != 0:
                res *= x
                n -= 1

            x *= x
            n //= 2
        
        res *= x
        return res

        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.myPow
            self.assertEqual(func(2.0, 10), 1024.0)
            self.assertAlmostEqual(func(2.1, 3), 9.261)
            self.assertEqual(func(2.0, -2), 0.25)


if __name__ == '__main__':
    unittest.main()