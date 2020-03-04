'''
04/03/2020

62. Unique Paths - Medium

Tag: Dynamic Programming

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

'''

# Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        DP
        Time:O(mxn)
        Space:O(mxn)
        '''
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        
        for r in range(1, m):
            dp[r][0] = dp[r-1][0]
        for c in range(1, n):
            dp[0][c] = dp[0][c-1]
            
            
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        return dp[m-1][n-1]
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().uniquePaths
        self.assertEqual(func(3, 2), 3)


        self.assertEqual(func(7, 3), 28)

if __name__ == '__main__':
    unittest.main()