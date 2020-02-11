'''
06/01/2020

926. Flip String to Monotone Increasing - Medium

Tag: Array, Prefix Sums

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

from typing import List
# Solution
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        n = len(S)
        # create prefix sums
        P = [0] * (n + 1)
        for idx, c in enumerate(S):
            P[idx+1] = P[idx] + int(c)
        
        res = n
        for idx in range(0, n+1):
            # number of 1 in S[0, idx):, first number of idx chars
            one_before_idx = P[idx]
            # number of 1 in S[idx, n):, later N-idx chars
            one_after_idx = P[n] - P[idx]
            # number of 0 in S[idx, n):
            # len(S[idx, n)) - one_after_idx
            zero_after_idx = n - idx - one_after_idx
            
            # for given idx, in order to make it Monotone,
            # we have to flip all the one before idx to zero,
            # and filp all the zero after idx to one.
            # total filp is one_before_idx+zero_after_idx
            res = min(res, one_before_idx+zero_after_idx)
        
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().minFlipsMonoIncr
        self.assertEqual(func("00110"), 1)
        self.assertEqual(func("010110"), 2)
        self.assertEqual(func("00011000"), 2)



if __name__ == '__main__':
    unittest.main()