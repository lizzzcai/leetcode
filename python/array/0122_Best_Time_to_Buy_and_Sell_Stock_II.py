'''
06/04/2020

122. Best Time to Buy and Sell Stock II - Easy

Tag: Array, Greedy

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
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
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Peak Valley Approach
        Time: O(n)
        Space: O(1)
        '''
        if not prices:
            return 0
        
        i = 0
        valley, peak = prices[0], prices[0]
        res = 0
        n = len(prices)
        
        while i < n -1:
            # find the valley
            while i < n-1 and prices[i] >= prices[i+1]:
                i+=1
            valley = prices[i]
            # find the peak
            while i < n-1 and prices[i] <= prices[i+1]:
                i+=1
            peak = prices[i]
            
            res += peak - valley
        
        return res

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        prev, res = 0, 0
        n = len(prices)
        for i in range(1, n):
            # if increasing continue
            if prices[i] >= prices[i-1] and prices[i] >= prices[prev]:
                continue
            else:
                res += prices[i-1] - prices[prev]
                prev = i
        
        # add the last block
        res += prices[-1] - prices[prev]
        
        return res

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Simple One Pass
        
        keep on adding the profit obtained from every consecutive transaction.
        
        Time: O(n)
        Space: O(1)
        '''
        if not prices:
            return 0
        
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        
        return res


class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        BF
        Time: O(n^n)
        Space: O(n)
        '''
        def calculate(s, n):
            if s >= n:
                return 0
            res = 0
            for start in range(s, n):
                max_profit = 0
                for i in range(start+1, n):
                    if prices[start] < prices[i]:
                        profit = calculate(i+1, n) + prices[i] - prices[start]
                        
                        if profit > max_profit:
                            max_profit = profit
                
                if max_profit > res:
                    res = max_profit
            
            return res
        
        return calculate(0, len(prices))

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2(),Solution3(), Solution4()]:
            func = Sol.maxProfit
            self.assertEqual(func([7,1,5,3,6,4]), 7)
            self.assertEqual(func([1,2,3,4,5]), 4)
            self.assertEqual(func([7,6,4,3,1]), 0)



if __name__ == '__main__':
    unittest.main()