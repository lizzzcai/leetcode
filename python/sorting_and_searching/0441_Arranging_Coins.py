'''
04/07/2020

441. Arranging Coins - Easy

Tag: Math, Binary Searh

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(logn)
    Space complexity : O(1)
    '''
    def arrangeCoins(self, n: int) -> int:
        '''
        
        1+2+3+4+..+n = n(n+1)/2
        k = n(n+1)/2
        
        '''
        
        l, r = 0, n
        while l <= r:
            mid = (l+r)//2
            k = mid*(mid+1)//2
            if k == n:
                return mid
            elif k > n:
                r = mid - 1
            else:
                l = mid + 1
        
        return r
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.arrangeCoins
            self.assertEqual(func(5), 2)
            self.assertEqual(func(8), 3)


if __name__ == '__main__':
    unittest.main()