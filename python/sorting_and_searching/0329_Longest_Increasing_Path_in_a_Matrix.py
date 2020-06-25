'''
26/06/2020

329. Longest Increasing Path in a Matrix - Hard

Tag: DFS, Topological Sort, Memoization

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(nm)
    Space complexity : O(nm)
    '''
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
        
        DFS + memo
        '''
        if not matrix:
            return 0
        R, C = len(matrix), len(matrix[0])
        memo = {}
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def dfs(i, j, R, C, matrix, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            for dr, dc in dirs:
                nr, nc = i+dr, j+dc
                if 0<=nr<R and 0<=nc<C and matrix[nr][nc] > matrix[i][j]:
                    res = max(res, dfs(nr,nc,R,C, matrix, memo))
    
            memo[(i,j)] = res + 1
            return memo[(i,j)]
        
        
        return max(dfs(i, j, R, C, matrix, memo) for i in range(R) for j in range(C))
            
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.longestIncreasingPath
            self.assertEqual(func([[9,9,4],[6,6,8],[2,1,1]]), 4)
            self.assertEqual(func([[3,4,5],[3,2,6],[2,2,1]]), 4)


if __name__ == '__main__':
    unittest.main()