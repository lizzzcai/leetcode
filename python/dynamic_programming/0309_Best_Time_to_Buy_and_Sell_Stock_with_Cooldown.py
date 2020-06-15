'''
13/06/2020

123. 309. Best Time to Buy and Sell Stock with Cooldown - Medium

Tag: Dynamic Programming

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp  = [0] * (n+1)
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
        # dp[i] = max(dp[i-1], prices[i] - prices[j] + dp[j-2]) j = [0, i-1]
        # If we sell the shares on i-th day bought on j-th day, 
        # we couldn't trade on (j-1)-th day because of cooldown. So the last one is dp[j-2].
        
        min_price = prices[0]
        for i in range(1, n+1):
            min_price = min(min_price, prices[i-1]-dp[i-2])
            dp[i] = max(dp[i-1], prices[i-1]-min_price)
        
        return dp[n]

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
            self.assertEqual(func([1,2,3,0,2]), 3)




if __name__ == '__main__':
    unittest.main()