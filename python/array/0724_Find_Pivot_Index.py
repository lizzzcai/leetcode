'''
28/01/2020

724. Find Pivot Index - Easy

Tag: Array, Prefix Sum

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
 

Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
 

'''

from typing import List
# Solution
class Solution1:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        Prefix Sum
        Time: O(n)
        Space: O(1)
        '''
        
        SUM = 0
        for num in nums:
            SUM += num
        
        # nums[0] + nums[1] +...+ nums[i-1] + nums[i] = nums[i] + nums[i+1] +...+ nums[n-1]
        # left_sum_i = nums[i] + right_sum_i+1
        # left_sum_i = SUM - left_sum_i + nums[i]
        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            if left_sum == SUM - left_sum + nums[i]:
                return i
        return -1


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        Prefix Sum
        Time: O(n)
        Space: O(1)
        '''
        
        sum_right = 0
        for num in nums:
            sum_right += num
        
        sum_left = 0
        for i, num in enumerate(nums):
            sum_left += num
            if sum_left == sum_right:
                return i
            sum_right -= num
        
        return -1
            

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().pivotIndex
        self.assertEqual(func([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(func([1, 2, 3]), -1)

        func = Solution2().pivotIndex
        self.assertEqual(func([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(func([1, 2, 3]), -1)

if __name__ == '__main__':
    unittest.main()