'''
14/03/2020

719. 153. Find Minimum in Rotated Sorted Array - Medium

Tag: Binary Search, Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

'''

from typing import List
# Solution
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        l,h = 0, len(nums)-1
        while l < h:
            mid = (l+h) // 2
            if nums[mid] < nums[h]:
                h = mid
            else:
                l = mid + 1
        
        return nums[l]

        
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findMin
            self.assertEqual(func([3,4,5,1,2]), 1)
            self.assertEqual(func([4,5,6,7,0,1,2]), 0)




if __name__ == '__main__':
    unittest.main()