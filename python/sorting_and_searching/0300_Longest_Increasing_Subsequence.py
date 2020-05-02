'''
21/03/2020

300. Longest Increasing Subsequence - Medium

Tag: Binary Search, Dynamic Programming, Array

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''

from typing import List
# Solution
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        binary search

        https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation

        Patience Sort
        https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf

        Time: O(NlogN)
        Space: O(N)
        '''
        
        n = len(nums)
        if n <= 1:
            return n
        
        # tails to store the last value of the smallest increasing subsequence of size idx
        # for i in tails[i], the increasing subsequence length is i+1
        tails = [0] * n
        # result
        size = 0
        for num in nums:
            # binary search
            l, r = 0, size-1
            while l <= r:
                mid = (l+r)//2
                # find the first value >= target
                if tails[mid] >= num:
                    r = mid - 1
                else:
                    l = mid + 1

            tails[l] = num
            size = max(size, l+1)
            
        return size
        
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Dynamic Programming
        Time: O(N^2)
        Space: O(N)
        '''
        
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
        

class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Patience sort
        Time: O(NlogN)
        Space: O(N)
        '''
        n = len(nums)
        if n <= 1:
            return n
        # num, pointer
        c = [(0,0)]*n
        size = 0
        
        def find_left(nums, right, target):
            l, r = 0, right-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid][0] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return l
        
        for x in nums:
            idx = find_left(c, size, x)
            c[idx] = (x, c[idx-1][0]) if idx > 0 else (x, 0)
            size = max(size, idx+1)

        LIS = [c[size-1][0]]
        for i in range(size-1, 0, -1):
            LIS.append(c[i][1])

        #print(LIS[::-1])
        return size

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.lengthOfLIS
            self.assertEqual(func([10,9,2,5,3,7,101,18]), 4)
            self.assertEqual(func([10]), 1)
            self.assertEqual(func([4,5,6,3]), 3)
            self.assertEqual(func([4,5,3,6]), 3)
            self.assertEqual(func([]), 0)



if __name__ == '__main__':
    unittest.main()