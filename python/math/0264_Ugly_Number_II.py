'''
05/04/2020

264. Ugly Number II - Medium

Tag: Math

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

'''

from typing import List
# Solution
class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        '''
        (1) 1x2,  2x2, 2x2, 3x2, 3x2, 4x2, 5x2...
        (2) 1x3,  1x3, 2x3, 2x3, 2x3, 3x3, 3x3...
        (3) 1x5,  1x5, 1x5, 1x5, 2x5, 2x5, 2x5...
        
        Time: O(n)
        '''
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1: # already have 1
            u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            min_u = min(u2,u3,u5)
            if min_u == u2:
                i2 += 1
            if min_u == u3:
                i3 += 1
            if min_u == u5:
                i5 += 1
            ugly.append(min_u)
            n -= 1

        return ugly[-1]
        
            
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.nthUglyNumber
            self.assertEqual(func(10), 12)
            self.assertEqual(func(1), 1)



if __name__ == '__main__':
    unittest.main()