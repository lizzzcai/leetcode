'''
19/04/2020

494. Target Sum - Medium

Tag: Dynamic Programming, DFS

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

'''
import math
from typing import List
import collections
# Solution
class Solution1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # +1000 to make sure all sum is >= 0
        memo = [[-math.inf]*2001 for _ in range(len(nums))]
        
        def calculate(nums, start, n, curr_sum, memo):
            if start == n:
                if curr_sum == S:
                    return 1
                else:
                    return 0
            
            
            if memo[start][curr_sum+1000] != -math.inf:
                return memo[start][curr_sum+1000]
            out = 0
            out += calculate(nums, start+1, n, curr_sum+nums[start], memo)
            out += calculate(nums, start+1, n, curr_sum-nums[start], memo)
            memo[start][curr_sum+1000] = out
            
            return out
        
        return calculate(nums, 0, len(nums), 0, memo)


class Solution2:
    '''
    TLE
    '''
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = collections.defaultdict(lambda: collections.defaultdict(int))
        
        def calculate(memo, start, curr_sum, N):
            if start == N:
                if curr_sum == S:
                    return 1
                else:
                    return 0
            
            if memo[start][curr_sum]:
                return memo[start][curr_sum]
            out = 0
            out += calculate(memo, start+1,curr_sum+nums[start], N)
            out += calculate(memo, start+1,curr_sum-nums[start], N)
            
            memo[start][curr_sum] = out
            
            return out
        
        
        return calculate(memo, 0, 0, len(nums))

class Solution3:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        DP
        Time: O(l*n) l == 2001
        Space:O(l*n)
        
        '''
        N = len(nums)
        #init the dp
        dp = [[0]*2001 for _ in range(N)]
        dp[0][nums[0]+1000] = 1
        dp[0][-nums[0]+1000] += 1
        
        for i in range(1, N):
            for _sum in range(-1000, 1000):
                if dp[i-1][_sum+1000]:
                    dp[i][_sum+nums[i]+1000] += dp[i-1][_sum+1000]
                    dp[i][_sum-nums[i]+1000] += dp[i-1][_sum+1000]
        
        if S > 1000:
            return 0
        else:
            return dp[N-1][S+1000]


class Solution4:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        1D - DP
        Time: O(l*n) l == 2001
        Space:O(l)
        
        '''
        if S > 1000:
            return 0
        
        #init the dp
        dp = [0]*2001
        dp[nums[0]+1000] = 1
        dp[-nums[0]+1000] += 1
        
        for i in range(1, len(nums)):
            dp1 = [0]*2001
            for _sum in range(-1000, 1000):
                if dp[_sum+1000]:
                    dp1[_sum+nums[i]+1000] += dp[_sum+1000]
                    dp1[_sum-nums[i]+1000] += dp[_sum+1000]
            dp = dp1
    

        return dp[S+1000]


class Solution5:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        1D - DP
        
        initially assign + to every number, then use dp to determine how many combination of flips from + to - are there to reach S.
        
        Time: O(l*n) l == 2001
        Space:O(l)
        
        
        '''
        if S > 1000:
            return 0
        
        _sum = sum(nums)
        if _sum < S or (_sum-S)%2 == 1:
            return 0
        
        target = (_sum-S) // 2
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(len(nums)):
            j = target
            while j >= nums[i]:
                dp[j] += dp[j-nums[i]]
                j -= 1
        
        
        return dp[target]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.findTargetSumWays
            self.assertEqual(func([1,1,1,1,1],3) ,5)
            self.assertEqual(func([6,20,22,38,11,15,22,30,0,17,34,29,7,42,46,49,30,7,14,5], 28), 6738)
            self.assertEqual(func([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 13), 0)

if __name__ == '__main__':
    unittest.main()