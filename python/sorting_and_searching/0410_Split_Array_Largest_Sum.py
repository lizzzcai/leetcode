'''
19/04/2020

Tag: Binary Search, Dynamic Programming

410. Split Array Largest Sum - Hard

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

'''

from typing import List
import math
class Solution1:
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        BF
        '''
        def helper(start, end, m):
            if start > end:
                return 0
            if m == 1:
                return sum(nums[start:end])
            

            min_sum = math.inf
            if m < 0:
                return min_sum
            
            for mid in range(start+1, end+1):
                left, right = sum(nums[start:mid]), helper(mid, end, m-1)
                min_sum = min(min_sum, max(left, right))
            
            return min_sum
        
        
        return helper(0, len(nums), m)




class Solution2:
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        bf with memo and early terminate
        '''
        memo = {}
        
        def helper(start, end, m):
            if start > end:
                return 0
            if m == 1:
                return sum(nums[start:end])
            

            min_sum = math.inf
            if m < 0:
                return min_sum
            
            if (start,m) in memo:
                return memo[(start,m)]
            
            for mid in range(start+1, end+1):
                left, right = sum(nums[start:mid]), helper(mid, end, m-1)
                min_sum = min(min_sum, max(left, right))
                if left > right:
                    break
            
            memo[(start,m)] = min_sum
            return memo[(start,m)]
        
        
        return helper(0, len(nums), m)

class Solution3:
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        bf + cumulative sum with memo and early terminate
        '''
        memo = {}
        cums = [0] * (len(nums)+1)
        for i in range(len(nums)):
            cums[i+1] = cums[i] + nums[i]


        def helper(start, end, m, cums, memo):
            if start > end:
                return 0
            if m == 1:
                return sum(nums[start:end])
            

            min_sum = math.inf
            if m < 0:
                return min_sum
            
            if (start,m) in memo:
                return memo[(start,m)]
            
            for mid in range(start+1, end+1):
                left, right = sum(nums[start:mid]), helper(mid, end, m-1, cums, memo)
                left, right = cums[mid]-cums[start], helper(mid, end, m-1, cums, memo)
                min_sum = min(min_sum, max(left, right))
                if left > right:
                    break
            
            memo[(start,m)] = min_sum
            return memo[(start,m)]
        
        
        return helper(0, len(nums), m, cums, memo)

class Solution4:
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        binary search

        https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation
        '''

        def is_valid(nums, m, mid):
            cuts, curr_sum = 1, 0
            for x in nums:
                curr_sum += x
                # make a cut
                if curr_sum > mid:
                    cuts, curr_sum = cuts+1, x
                #if cuts > m:
                #    return False
            return cuts <= m
        
        low, high = max(nums), sum(nums)

        while low <= high:
            mid = (low + high) // 2
            if is_valid(nums, m, mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(),Solution3(), Solution4()]:
            func = Sol.splitArray
            self.assertEqual(func([7,2,5,10,8], 2), 18)
            self.assertEqual(func([7,2,5,10,8,3,6,10,8,100,101], 4), 101)

if __name__ == '__main__':
    unittest.main()