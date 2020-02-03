'''
04/02/2020

15. 3Sum - Medium

Tag: Array, Two Pointers

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

from typing import List
# Solution
class Solution:
    '''
    Time complexity : O(n^2)
    Space complexity : O(1)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_== 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum_ < 0:
                    l += 1
                else: # sum_ > 0
                    r -= 1
        
        return res
                
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().threeSum
        self.assertEqual(func([-1, 0, 1, 2, -1, -4]), [[-1,-1,2],[-1,0,1]])

if __name__ == '__main__':
    unittest.main()