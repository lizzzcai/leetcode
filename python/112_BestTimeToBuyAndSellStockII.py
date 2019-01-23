'''
23/01/2019

Tag: Array

112. Best Time to Buy and Sell Stock II - Easy


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

# Solution
class Solution:
    '''
    Time complexity : O(n). 
    Space complexity : O(1). 
    '''
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) == 0:
            return 0
        n = len(prices)
        prev = 0
        maxprofit = 0
        for i in range(1, n):
            # need to sum the max difference in each ascending array block.
            if prices[i] >= prices[prev] and prices[i] >= prices[i-1]:
                continue
            else:
                maxprofit += prices[i-1] - prices[prev]
                prev = i
        # add the last ascending block, if prev == n-1, will be 0
        maxprofit += prices[n-1] - prices[prev]
        return maxprofit
                
            
        
# Unit Test
import unittest
class maxProfitCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_maxProfit(self):
        func = Solution().maxProfit
        self.assertEqual(func([7,1,5,3,6,4]), 7)
        self.assertEqual(func([1,2,3,4,5]), 4)
        self.assertEqual(func([7,6,4,3,1]), 0)

if __name__ == '__main__':
    unittest.main()