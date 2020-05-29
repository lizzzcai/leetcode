'''
29/05/2020

795. Number of Subarrays with Bounded Maximum - Medium

Tag: Array

We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].

'''

from typing import List
# Solution
class Solution1:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        '''
        https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/434194/Very-simple-Python3-and-C%2B%2B-with-explanation
        O(n)
        O(1)
        
        the value of the maximum array element in that subarray is at least L and at most R
        '''
        res = 0
        i = 0
        prev = 0
        for j, x in enumerate(A):
            if L <= x <= R:
                prev = j - i + 1
                res += prev
            elif x < L:
                res += prev
            else:
                prev = 0
                i = j + 1
        
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
            func = Sol.numSubarrayBoundedMax
            self.assertEqual(func([2, 1, 4, 3], 2, 3), 3)

if __name__ == '__main__':
    unittest.main()