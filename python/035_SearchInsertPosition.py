'''

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

# Solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # indicate the left and right of the nums list
        left, right = 0, len(nums) - 1
        if target < nums[left]:
            # insert in the first index
            return 0
        if target > nums[right]:
            # insert after the last index
            return right + 1
        while left < right:
            # find the index of mid value
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return left
                


# Unit Test
import unittest
class SearchInsertPositionCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_twoSum(self):
        func = Solution().searchInsert
        self.assertEqual(func([1,3,5,6], 5), 2)
        self.assertEqual(func([1,3,5,6], 2), 1)
        self.assertEqual(func([1,3,5,6], 7), 4)
        self.assertEqual(func([1,3,5,6], 0), 0)
        
if __name__ == '__main__':
    unittest.main()