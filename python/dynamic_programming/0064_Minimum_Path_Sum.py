'''
19/04/2020

64. Minimum Path Sum - Medium

Tag: Dynamic Programming, Array

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

'''
import math
from typing import List
import collections
# Solution
class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        # assign value for the fist row and first col
        for r in range(1, len(grid)):
            dp[r][0] +=dp[r-1][0] + grid[r][0]
        for c in range(1, len(grid[0])):
            dp[0][c] +=dp[0][c-1] + grid[0][c]
        
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                dp[r][c] += min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        
        return dp[len(grid)-1][len(grid[0])-1]


# Solution
class Solution2:
    '''
    DP
    Time: O(mn)
    Space: O(mn)
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        R, C = len(grid), len(grid[0])
        dp = [[0]*C for _ in range(R)]

        for r in range(0, R):
            for c in range(0, C):
                # assign value for the fist col
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                elif r == 0 and c != 0:
                    dp[r][c] +=dp[r][c-1] + grid[r][c]
                # assign value for the fist row 
                elif r != 0 and c == 0:
                    dp[r][c] +=dp[r-1][c] + grid[r][c]
                else:
                    dp[r][c] += min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        
        return dp[R-1][C-1]


# Solution
class Solution3:
    '''
    DP
    Time: O(mn)
    Space: O(1)
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        R, C = len(grid), len(grid[0])

        for r in range(0, R):
            for c in range(0, C):
                # assign value for the fist col
                if r == 0 and c == 0:
                    grid[r][c] = grid[r][c]
                elif r == 0 and c != 0:
                    grid[r][c] +=grid[r][c-1]
                # assign value for the fist row 
                elif r != 0 and c == 0:
                    grid[r][c] +=grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        return grid[R-1][C-1]


class Solution4:
    '''
    DP with memo
    Time: O(mn)
    Space: O(mn)
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        memo = [[0]*n for _ in range(m)]
        
        def helper(grid, r, c, memo):
            
            if r == len(grid)-1 and c == len(grid[0])-1:
                # memo[r][c] = grid[r][c]
                return grid[r][c]
            
            if memo[r][c]:
                return memo[r][c]
            
            row_min = math.inf
            col_min = math.inf
            
            if r < len(grid)-1:
                row_min = helper(grid,r+1,c,memo)
            if c < len(grid[0]) -1:
                col_min = helper(grid,r,c+1,memo)
            
            memo[r][c] = min(row_min, col_min) + grid[r][c]
            return memo[r][c]

            
        
        return helper(grid,0,0,memo)


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2(),Solution3(),Solution4()]:
            func = Sol.minPathSum
            self.assertEqual(func([[1,3,1],[1,5,1],[4,2,1]]) ,7)
            self.assertEqual(func([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]) ,85)
if __name__ == '__main__':
    unittest.main()