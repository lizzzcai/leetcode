'''
14/03/2020

69. Sqrt(x) - Easy

Tag: 

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

'''

from typing import List

# Binary search
class Solution1:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            temp = mid*mid
            if temp == x:
                return mid
            elif temp > x:
                r = mid - 1
            else:
                l = mid + 1
        
        return r


class Solution2:
    def mySqrt(self, x: int) -> int:
        '''
        newton method
        https://blog.csdn.net/WitsMakeMen/article/details/81061217
        
        
        '''
        r = x
        while r*r > x:
            # xk+1 = xk - f(xk)/f'(xk)
            #r = r - (r*r-x)/(2*r)
            r = (r + x/r) // 2
            
        return int(r)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.mySqrt
            self.assertEqual(func(4), 2)
            self.assertEqual(func(8), 2)
            self.assertEqual(func(10), 3)
            self.assertEqual(func(1), 1)
            self.assertEqual(func(11), 3)



if __name__ == '__main__':
    unittest.main()