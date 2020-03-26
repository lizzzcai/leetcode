'''
26/03/2020

377. Combination Sum IV - Mdium

Tag: Dynamic Programming

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

'''

from typing import List
# Solution

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        Recursion

        slow
        '''
        if target == 0:
            return 1
        
        res = 0
        for num in nums:
            if target >= num:
                res += self.combinationSum4(nums, target-num)
        
        return res

class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        dp
        top-down


        for a DP solution, we just need to figure out a way to store the intermediate results, to avoid the same combination sum being calculated many times. 
        We can use an array to save those results, and check if there is already a result before calculation. 
        We can fill the array with -1 to indicate that the result hasn't been calculated yet. 0 is not a good choice because it means there is no combination sum for the target.

        '''
        def helper(nums, target):
            if dp[target] != -1:
                return dp[target]
            
            res = 0
            for num in nums:
                if target >= num:
                    res += helper(nums, target-num)
            
            dp[target] = res
            return res
                
        
        dp = [-1] * (target+1)
        dp[0] = 1
        
        return helper(nums, target)



class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        dp
        bottom-up
        Time: O(MN)
        space(M)
        
        similar: https://leetcode.com/problems/coin-change-2/


        https://leetcode.com/problems/combination-sum-iv/discuss/85036/1ms-Java-DP-Solution-with-Detailed-Explanation
        
        '''
        dp = [0] * (target+1)
        #dp[0] = 1
        for num in nums:
            if num <= target:
                dp[num] = 1
        '''
        Think 'add coins to a target' as every time to introduce a new coin to realize 1-n target. Think this one as every time to use all possible coins to realize 1-n target. 
        For example, if we have coins '2' and '3', in 'add coins to a target' case, target 5 is realized by out loop either on coin 2 or coin 3 depending on which one comes later, so dp[5]=1. This one dp[5] is calculated when both dp[2] and dp[3]==1, so dp[5]=2.
        
        '''
        for i in range(target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]
        
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
            func = Sol.combinationSum4
            self.assertEqual(func([1,2,3], 4), 7)
            self.assertEqual(func([1,2,3], 20), 121415)
            self.assertEqual(func([4,2,1], 32), 39882198)



if __name__ == '__main__':
    unittest.main()