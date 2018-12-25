'''
25/12/2018

Tag: Binary Search

35. Search Insert Position - Easy

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

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

class Solution:
    '''
    Time Complexity: O(logn). 
    Space Complexity: O(1).
    '''
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if target < nums[left]:
            # insert in the first index
            return 0
        if target > nums[right]:
            # insert after the last index
            return right + 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # first value larger than the target, insert in this position.
        return left


# Unit Test
import unittest
class SearchInsertPositionCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_SearchInsertPosition(self):
        func = Solution().searchInsert
        self.assertEqual(func([1,3,5,6], 5), 2)
        self.assertEqual(func([1,3,5,6], 2), 1)
        self.assertEqual(func([1,3,5,6], 7), 4)
        self.assertEqual(func([1,3,5,6], 0), 0)
        
if __name__ == '__main__':
    unittest.main()