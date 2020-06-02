'''
02/06/2020

416. Partition Equal Subset Sum - Medium

Tag: Dynamic Programming

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
 

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(nm)
    Space complexity : O(nm)
    '''
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        s = s // 2
        
        '''
        https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
        
        Let us assume dp[i][j] means whether the specific sum j can be gotten from the first i numbers. 
        If we can pick such a series of numbers from 0-i whose sum is j, dp[i][j] is true, otherwise it is false.
        
        the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        '''
        n = len(nums)
        dp = [[False]*(s+1) for _ in range(n+1)]
        
        # base case
        dp[0][0] = True
        for i in range(1, n):
            dp[i][0] = True # we don't pick any number, sum is still 0
        
        for i in range(1, n+1):
            for j in range(1, s+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][s]

class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        s = s // 2
        
        '''
        https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
        
        Let us assume dp[i][j] means whether the specific sum j can be gotten from the first i numbers. 
        If we can pick such a series of numbers from 0-i whose sum is j, dp[i][j] is true, otherwise it is false.
        
        the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        '''
        n = len(nums)
        dp = [False]*(s+1)
        
        # base case
        dp[0] = True
        
        '''
        Every loop of nums refreshes dp array. We might get dp[i] from dp[i-num] whose index is smaller than i. 
        If we increase the index of sum from 0 to sum, we will get dp[i] from dp[i-num] , while dp[i-num] has been updated in this loop. 
        This dp[i-num] is not the number we got from the previous loop.
        '''
        for i in range(1, n+1):
            for j in range(s, 0, -1):
                if j >= nums[i-1]:
                    dp[j] = dp[j] or dp[j-nums[i-1]]
        
        return dp[s]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.canPartition
            self.assertEqual(func([1, 5, 11, 5]), True)
            self.assertEqual(func([1,2,3,5]), False)


if __name__ == '__main__':
    unittest.main()