'''
27/01/2020

560. Subarray Sum Equals K - Medium

Tag: Array, Hash Table, Prefix Sum

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''

from typing import List
# Solution
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        cummulated sum
        time: O(n^2)
        space:O(n)
        '''
        count = 0
        n = len(nums)
        P = [0] * (n+1)
        
        for i in range(n):
            P[i+1] = nums[i] + P[i]
        
        for i in range(n+1):
            for j in range(i+1, n+1):
                if P[j] - P[i] == k:
                    count += 1
        return count


class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        without space, accumulated sum
        time: O(n^2)
        space: O(1)
        
        '''
        count = 0
        n = len(nums)
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += nums[j]
                if sum_ == k:
                    count += 1
        return count


class Solution3:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        hash map
        https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example

        time: O(n)
        space: O(n)
        
        '''
        count = 0
        sum_ = 0
        n = len(nums)
        
        hmap = {0:1}
        for i in range(n):
            sum_ += nums[i]
            key = sum_ - k
            if key in hmap:
                count += hmap[key]
            hmap[sum_] = hmap.setdefault(sum_, 0) + 1
            
        return count

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution3().subarraySum
        self.assertEqual(func([1, 1, 1], 2), 2)
        self.assertEqual(func([1,1,1,4,32, 5, 3, 2, 1, 3, 2, 1, 1, 2, 0 ,0 ,1 ,1], 2), 11)


if __name__ == '__main__':
    unittest.main()