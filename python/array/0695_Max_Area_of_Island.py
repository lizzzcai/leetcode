'''
06/04/2020

695. Max Area of Island - Medium

Tag: Array, DFS

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

from typing import List
import collections
# Solution
class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        DFS
        Time O(mn)
        Space O(1)
        
        '''
        if not grid:
            return 0
        nRows = len(grid)
        nCols = len(grid[0])
        
        def dfs(r, c, R, C):
            if 0<=r<R and 0<=c<C and grid[r][c] == 1:
                grid[r][c] = -1 # visited
                out = 1 # current cell 
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    out += dfs(r+dr,c+dc,R,C)
                return out
            else:
                return 0
        
        res = 0
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c,nRows,nCols))
        
        return res

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        DFS + Stack
        Time O(mn)
        Space O(1)
        
        '''
        if not grid:
            return 0
        nRows = len(grid)
        nCols = len(grid[0])
        
        
        res = 0
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 1:
                    area = 0
                    stack = [(r,c)]
                    grid[r][c] = -1
                    while stack:
                        i, j = stack.pop()
                        area += 1
                        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                            if 0<=i+dr<nRows and 0<=j+dc<nCols and grid[i+dr][j+dc] == 1:
                                stack.append((i+dr,j+dc))
                                grid[i+dr][j+dc] = -1
                    res = max(res, area)
        
        return res


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.maxAreaOfIsland
            self.assertEqual(func([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]), 4)
            self.assertEqual(func([[0,0,0,0,0,0,0,0]]), 0)
            self.assertEqual(func([[0,0,0,1,1,1,0,0]]), 3)


if __name__ == '__main__':
    unittest.main()