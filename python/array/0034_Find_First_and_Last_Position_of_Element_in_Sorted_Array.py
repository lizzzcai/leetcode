'''
16/01/2019

Tag: Binary Search, Array

34. Find First and Last Position of Element in Sorted Array - Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


'''

from typing import List

class Solution:
    '''
    Time Complexity: O(logn). 
    Space Complexity: O(1).
    '''
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        if first <= last:
            return [first, last]
        else:
            return [-1, -1]
        
    # find left boundary
    def findFirst(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, mid, right = 0, 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else: # nums[mid] <= target
                # nums[mid] == target, right boundary step in to skip the duplicate value in the right
                # when reach the condition: nums[mid] < target, left will be the first value statisfy the condition
                right = mid - 1
        return left

    # find right boundary
    def findLast(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, mid, right = 0, 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # skip the duplicate value in the left
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right


class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        left = self.find_left(nums, target)
        right = self.find_right(nums, target)
        
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]
    
    def find_left(self, nums, target):
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
    
    def find_right(self, nums, target):
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
                
        return r

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                left = i
                break
        
        if left == -1:
            return [-1, -1]
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                right = i
                break
        
        return [left, right]
            

# Unit Test
import unittest
class SearchRangeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_SearchRange(self):
        func = Solution1().searchRange
        self.assertEqual(func([5,7,7,8,8,10], 8), [3,4])
        self.assertEqual(func([5,7,7,8,8,10], 6), [-1,-1])
        self.assertEqual(func([1], 6), [-1,-1])
        self.assertEqual(func([1], 1), [0,0])
        self.assertEqual(func([], 1), [-1,-1])



        
if __name__ == '__main__':
    unittest.main()