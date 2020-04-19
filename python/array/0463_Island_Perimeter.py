'''
18/04/2020

463. Island Perimeter - Easy

Tag: Array, DFS, Hash Table

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


'''

from typing import List
import collections
# Solution
class Solution1:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        DFS
        Time O(mn)
        Space O(1)

        '''
        if not grid:
            return 0
        
        def dfs(r, c, R, C):
            # if outside the boundary
            if r == -1 or r == R or c == -1 or c == C:
                return 1
            
            if 0<=r<R and 0<=c<C and grid[r][c] != -1:
                if grid[r][c] == 1:
                    grid[r][c] = -1 # mark visted
                    out = 0
                    for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                        out += dfs(r+dr,c+dc,R,C)
                    return out
                else: # 0
                    return 1
            else:
                return 0

        
        
        nRows = len(grid)
        nCols = len(grid[0])
        
        res = 0
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 1:
                    res += dfs(r,c,nRows,nCols)
        
        return res



class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        iterative
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
                     for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                            nr,nc = r+dr,c+dc
                            if nr == -1 or nr == nRows or nc == -1 or nc == nCols:
                                res += 1
                            elif grid[nr][nc] == 0:
                                res += 1
        return res
                    


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.islandPerimeter
            self.assertEqual(func([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,1,1]]), 20)
            self.assertEqual(func([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]), 16)


if __name__ == '__main__':
    unittest.main()