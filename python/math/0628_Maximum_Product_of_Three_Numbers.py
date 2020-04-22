'''
22/04/2020

628. Maximum Product of Three Numbers - Easy

Tag: Array, Math

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

from typing import List
import math
# Solution
class Solution1:
    def maximumProduct(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/maximum-product-subarray/discuss/183483/In-Python-it-can-be-more-concise-PythonC%2B%2BJava
        
        Time: O(n)
        space O(1)
        '''
        

        
        min1 = min2 = math.inf
        max1 = max2 = max3 = -math.inf
    
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n
            
            if n >= max1: # greater than max1, max2, max3
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2: # between max2 and max3
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n
        
        return max(min1*min2*max1, max1*max2*max3)


class Solution2:
    def maximumProduct(self, nums):
            nums.sort()
            return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])  

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.maximumProduct
            self.assertEqual(func([1,2,3]), 6)
            self.assertEqual(func([1,2,3,4]), 24)
            self.assertEqual(func([-4,-3,-2,-1,60]), 720)

if __name__ == '__main__':
    unittest.main()