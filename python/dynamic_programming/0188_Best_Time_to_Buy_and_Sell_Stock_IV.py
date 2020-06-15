'''
13/06/2020

188. Best Time to Buy and Sell Stock IV - Hard

Tag: Dynamic Programming

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(min(kn, n^2/2))
    Space complexity : O(kn)
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java
        if k > len(prices)//2:
            return self.bf(prices)
        
        dp = [[0]*(len(prices)+1) for _ in range(k+1)]
        
        # dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1][j-1]) for j = [0, i-1]
        for j in range(1, k+1):
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
                min_val = min(min_val, prices[i-1] - dp[j-1][i-1])
                dp[j][i] = max(dp[j][i-1], prices[i-1]-min_val)
        
        return dp[k][len(prices)]
    
    
    def bf(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
                
        return profit


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
            self.assertEqual(func([2,4,1],2), 2)
            self.assertEqual(func([3,2,6,5,0,3],2), 7)


if __name__ == '__main__':
    unittest.main()