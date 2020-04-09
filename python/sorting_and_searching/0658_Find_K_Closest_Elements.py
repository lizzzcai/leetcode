'''
08/04/2020

658. Find K Closest Elements - Medium

Tag: Binary Search

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.

'''

from typing import List
# Solution
class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        Time: O(n+nlogn+klogk)
        Space: O(n)
        '''
        dist = [(abs(i-x), i) for i in arr]
        dist.sort()

        return sorted([t[1] for t in dist[:k]])
        
class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        Time: O(logn + k)
        Space: O(k)
        '''
        def binary_search(l, r, target):
            '''
            find the first element >= than target
            '''
            while l <= r:
                mid = (l+r) // 2
                if arr[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return l
        
        
        if x <= arr[0]:
            return arr[:k]
        
        if x >= arr[-1]:
            return arr[-k:]
        
        n = len(arr)
        idx = binary_search(0, n-1, x)
        
        l, r = max(0, idx-k), min(n-1, idx+k)
        
        while l+k <= r:
            # If there is a tie, the smaller elements are always preferred.
            if x - arr[l] <= arr[r] - x:
                r -= 1
            else:# x - arr[l] > arr[r] - x:
                l += 1
        
        return arr[l:r+1]


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.findClosestElements
            self.assertEqual(func([1,2,3,4,5], 4, 3), [1,2,3,4])
            self.assertEqual(func([1,2,3,4,5], 4, -1), [1,2,3,4])
            self.assertEqual(func([0,0,1,2,3,3,4,7,7,8], 3, 5), [3,3,4])
            self.assertEqual(func([0,1,2,2,2,3,6,8,8,9], 5, 9), [3,6,8,8,9])

if __name__ == '__main__':
    unittest.main()