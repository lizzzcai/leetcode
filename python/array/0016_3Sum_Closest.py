'''
06/02/2020

16. 3Sum Closest - Medium

Tag: Array, Two Pointers

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

from typing import List
# Solution
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        Time: O(n^2)
        Space: O(1)
        '''
        nums.sort()
        n = len(nums)
        if n < 3:
            return
        res = nums[0] + nums[1] + nums[2]
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                elif s > target:
                    # skip duplicates
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                else: # s < target
                    # skip dulicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                # update the res of closer
                if abs(target - s) < abs(target - res):
                    res = s

        return res
                    
                
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().threeSumClosest
        self.assertEqual(func([-1, 2, 1, -4], 1), 2)

if __name__ == '__main__':
    unittest.main()