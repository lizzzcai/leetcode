'''
07/09/2020

474. Ones and Zeroes - Medium

Tag: Dynamic Programming

Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100

'''
import collections
from typing import List
# Solution
class Solution1:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        https://leetcode.com/problems/ones-and-zeroes/discuss/95807/0-1-knapsack-detailed-explanation.
        Time: O(mnk)
        '''
        counters = [collections.Counter(x) for x in strs]
        l = len(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(l+1)]

        for k in range(0, l+1):
            if k > 0:
                num_zeros = counters[k-1]['0']
                num_ones = counters[k-1]['1']
            for i in range(0, m+1):
                for j in range(0, n+1):
                    if k == 0:
                        dp[k][i][j] = 0
                    elif i >= num_zeros and j >= num_ones:
                        dp[k][i][j] = max(dp[k-1][i][j], dp[k-1][i-num_zeros][j-num_ones]+1)
                    else:
                        dp[k][i][j] = dp[k-1][i][j]
        
        return dp[l][m][n]
                    
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findMaxForm
            self.assertEqual(func(["10","0001","111001","1","0"], 5, 3), 4)
            self.assertEqual(func(["10","0","1"], 1, 1), 2)


if __name__ == '__main__':
    unittest.main()