'''
11/02/2020

518. Coin Change 2 - Medium

Tag: Dynamic Programming

ou are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
 

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
'''

from typing import List
# Solution
class Solution:
    
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        Time: O(n*m)
        Space:O(m)
        '''
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        
        return dp[amount]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().change
        self.assertEqual(func(5, [1, 2, 5]), 4)
        self.assertEqual(func(3, [2]), 0)
        self.assertEqual(func(10, [10]), 1)



if __name__ == '__main__':
    unittest.main()