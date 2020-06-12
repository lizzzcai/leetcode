'''
11/06/2020

35. Search Insert Position - Easy

Tag: Binary Search, Array

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

'''

from typing import List
# Solution
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if nums[l] >= target:
            return l
        if nums[r] < target:
            return r+1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return l

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.searchInsert
            self.assertEqual(func([1,3,5,6], 5), 2)
            self.assertEqual(func([1,3,5,6], 2), 1)
            self.assertEqual(func([1,3,5,6], 7), 4)
            self.assertEqual(func([1,3,5,6], 0), 0)


if __name__ == '__main__':
    unittest.main()