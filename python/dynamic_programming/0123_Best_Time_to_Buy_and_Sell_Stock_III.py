'''
13/06/2020

123. Best Time to Buy and Sell Stock III - Hard

Tag: Array Dynamic Programming

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(kn)
    Space complexity : O(kn)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[0]*(len(prices)+1) for _ in range(3)]
        
        # dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1][j-1]) for j = [0, i-1]
        for k in range(1, 3):
            min_val = prices[0]
            for i in range(1, len(prices)+1):
                '''
                https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
                for (int j=1;j<=i;j++){
                min=Math.min(min, prices[j]-dp[k-1][j-1]);
                }
                In this step, we compute min of prices[j]-dp[k-1][j-1] for j in range [1, i]. However, the results in the range [1, i-1] are independent with i, and have already been computed in previous loop when i = i-1. 
                I mean, when i updates from i-1 to i, we only have one new case: prices[i]-dp[k-1][i-1]. Emmm...hard to explain, I hope you can get some inspirations from my word and go back to try to understand it...
                '''
                min_val = min(min_val, prices[i-1]-dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i-1]-min_val)
        
        return dp[2][len(prices)]
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.maxProfit
            self.assertEqual(func([3,3,5,0,0,3,1,4]), 6)
            self.assertEqual(func([1,2,3,4,5]), 4)
            self.assertEqual(func([7,6,4,3,1]), 0)



if __name__ == '__main__':
    unittest.main()