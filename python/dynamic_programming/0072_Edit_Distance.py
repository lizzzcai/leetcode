'''
01/06/2020

72. Edit Distance - Hard

Tag: String, Dynamic Programming

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

from typing import List
# Solution
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        time: O (mn)
        space: O (mn)
        '''
        w1, w2 = '#'+word1, '#'+word2
        n1, n2 = len(w1), len(w2)
        
        dp = [[0]*n2 for _ in range(n1)]
        
        # second string is empty, we delete string 1
        for i in range(n1):
            dp[i][0] = i
        
        # first string is emty so we insert to string 1
        for i in range(n2):
            dp[0][i] = i
        
        for i in range(1, n1):
            for j in range(1, n2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(w1[i] != w2[j]))
        
        return dp[n1-1][n2-1]
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.minDistance
            self.assertEqual(func('horse', 'ros'), 3)
            self.assertEqual(func('intention', 'execution'), 5)


if __name__ == '__main__':
    unittest.main()