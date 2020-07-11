'''
01/07/2020

496. Next Greater Element I - Easy

Tag: Easy

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(nm)
    Space complexity : O(m)
    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # to store the index of given value in nums2
        arr = dict()
        for idx, x in enumerate(nums2):
            arr[x] = idx
        
        n = len(nums1)
        res = [-1]*n
        
        for idx in range(n):
            start = nums1[idx]
            for i in range(arr[start]+1, len(nums2)):
                if nums2[i] > start:
                    res[idx] = nums2[i]
                    break
            
        return res
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.nextGreaterElement
            self.assertEqual(func([4,1,2],[1,3,4,2]), [-1,3,-1])
            self.assertEqual(func([2,4],[1,2,3,4]), [3,-1])

if __name__ == '__main__':
    unittest.main()