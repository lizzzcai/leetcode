'''
22/04/2020

152. Maximum Product Subarray - Medium

Tag: Array, Dynamic Programming

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

from typing import List
# Solution
class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/maximum-product-subarray/discuss/183483/In-Python-it-can-be-more-concise-PythonC%2B%2BJava
        
        Time: O(n)
        space O(1)
        '''
        
        prefix, suffix, max_so_far = 0, 0, nums[0]
        
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_so_far = max(max_so_far, prefix, suffix)
        
        return max_so_far
class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/maximum-product-subarray/discuss/118535/C++-DP-Solution-using-2-Arrays
        
        Time: O(n)
        space O(1)
        '''
        
        dpmax, dpmin = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            k = dpmax * nums[i]
            m = dpmin * nums[i]
            dpmax = max(nums[i], k, m)
            dpmin = min(nums[i], k, m)
            
            res = max(res, dpmax)

        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.maxProduct
            self.assertEqual(func([2,3,-2,4]), 6)
            self.assertEqual(func([-2,0,-1]), 0)

if __name__ == '__main__':
    unittest.main()