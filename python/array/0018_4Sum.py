'''
06/01/2020

18. 4Sum - Medium

Tag: 


Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''

from typing import List
# Solution
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        left right pointers
        Time: O(n^3)
        Space O(1)
        
        '''
        # sort the nums for easy left right pointers
        nums.sort()
        n = len(nums)
        res = []
        if n < 4:
            return res
        i_a, i_d = 0, n-1
        # fix the d
        for i_d in range(n-1, 2, -1): # i_d from [3, n-1]
            # take advantage of the sorted array
            if nums[i_d]*4 < target:
                break
            # skip the duplicates of d
            if i_d < n-1 and nums[i_d] == nums[i_d+1]:
                continue
            # calculate the new target for 3 sums
            target_abc = target - nums[i_d]
            # start 3 sum here, by fixing a and adjust left right pointers b and c
            for i_a in range(i_d-2):
                # take advantage of the sorted array
                if nums[i_a]*3 > target_abc:
                    break
                # skip the duplicates of a
                if i_a > 0 and nums[i_a-1] == nums[i_a]:
                    continue
                # set up left right pointers
                i_b, i_c = i_a+1, i_d-1
                while i_b < i_c:
                    sum_abc = nums[i_a] + nums[i_b] + nums[i_c]
                    if sum_abc == target_abc:
                        res.append([nums[i_a], nums[i_b], nums[i_c], nums[i_d]])
                        # update idx_b and idx_c to skip duplicates of b and c
                        while i_b < i_c and nums[i_b] == nums[i_b+1]:
                            i_b += 1
                        while i_b < i_c and nums[i_c] == nums[i_c-1]:
                            i_c -= 1
                        i_b += 1
                        i_c -= 1
                    elif sum_abc > target_abc:
                        i_c -= 1
                    else: # sum_abc < target_abc
                        i_b += 1
        
        return res


class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        recursion
        Time: O(n^3)
        
        '''
        # sort nums for two pointers
        nums.sort()
        n = len(nums)
        res = []
        self.findNSum(nums, 0, n-1, 4, target, [], res)
        return res
        
    
    def findNSum(self, nums, left, right, N, target, result, results):
        # early termination
        if right-left+1 < N or N < 2 or nums[left]*N > target or nums[right]*N < target:
            return
        if N == 2:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    results.append(result + [nums[left], nums[right]])
                    # skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    #while left < right and nums[right] == nums[right-1]:
                    #    right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else: # s > target
                    right -= 1
        else:
            for i in range(left, right):
                # skip duplicatws
                if i > left and nums[i] == nums[i-1]:
                    continue
                else:
                    self.findNSum(nums, i+1, right, N-1, target-nums[i], result+[nums[i]], results)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().fourSum
        self.assertEqual(func([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        self.assertEqual(func([5,5,3,5,1,-5,1,-2], 4), [[-5,1,3,5]])
        self.assertEqual(func([-3,-1,0,2,4,5], 0), [[-3,-1,0,4]])

        func = Solution2().fourSum
        self.assertEqual(func([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        self.assertEqual(func([5,5,3,5,1,-5,1,-2], 4), [[-5,1,3,5]])
        self.assertEqual(func([-3,-1,0,2,4,5], 0), [[-3,-1,0,4]])

if __name__ == '__main__':
    unittest.main()