'''
06/01/2020

209. Minimum Size Subarray Sum - Medium

Tag: Array, Two Pointers, Binary Search

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

'''

from typing import List


class Solution1:
    '''
    Time:O(n)
    space:O(1)
    '''
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        # init the length of the nums and the result to return
        n = len(nums)
        min_len = n+1
        
        left = 0
        sum_val = 0
        
        for right in range(n):
            sum_val += nums[right]
            
            while sum_val >= s:
                min_len = min(min_len, right - left + 1)
                sum_val -= nums[left]
                left += 1
        
        if min_len == n + 1:
            return 0
        
        return min_len

class Solution2:
    '''
    Time:O(nlogn)
    space:O(n)
    '''
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        n = len(nums)
        sums = [0] * (n+1)
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]
        
        min_len = n+1
        
        for i in range(len(sums)):
            end = self.binarysearch(i+1, len(sums)-1, sums, s+sums[i])    
            if end == len(sums):
                break
            if end - i < min_len:
                min_len = end - i
        
        if min_len == n+1:
            return 0
        return min_len
    
    def binarysearch(self, l, r, nums, target):
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= target:
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
        func = Solution1().minSubArrayLen
        self.assertEqual(func(7, [2,3,1,2,4,3]), 2)
        self.assertEqual(func(100, [2,3,1,2,4,3]), 0)

        func = Solution2().minSubArrayLen
        self.assertEqual(func(7, [2,3,1,2,4,3]), 2)
        self.assertEqual(func(100, [2,3,1,2,4,3]), 0)

if __name__ == '__main__':
    unittest.main()