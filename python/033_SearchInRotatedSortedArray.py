'''
25/12/2018

Tag: Binary Search

33. Search in Rotated Sorted Array - Medium


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


'''

def binarySearch(arr, target):
    left , right = 0, len(arr) - 1  
    while left <= right:            
        mid = (left+right)//2
        # mid = left + (right-left)//2 # avoid overflow
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1 
    return -1

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if found target value, return the index
            if nums[mid] == target:
                return mid
            
            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[left]: # left rotated
                # in ascending order side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right rotated
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1

# Unit Test
import unittest
class SearchInRotatedSortedArrayCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_SearchInRotatedSortedArray(self):
        func = Solution().search
        self.assertEqual(func([4,5,6,7,0,1,2], 0), 4)
        self.assertEqual(func([4,5,6,7,0,1,2], 3), -1)

if __name__ == '__main__':
    unittest.main()