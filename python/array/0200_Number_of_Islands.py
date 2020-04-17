'''
06/04/2020

200. Number of Islands - Medium

Tag: BFS, DFS, Union Find

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    dfs
    Time complexity : O(mn)
    Space complexity : O(mn)
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(r,c):
            if r<0 or r >= len(grid) or c<0 or c>= len(grid[0]) \
                or grid[r][c] == '0' or visited[r][c]:
                return
            
            visited[r][c] = True
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(r+dr,c+dc)
        
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not visited[r][c] and grid[r][c] == '1':
                    dfs(r,c)
                    count += 1
        
        return count
        

class Solution2:
    '''
    dfs
    Time complexity : O(mn)
    Space complexity : O(1)
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(r,c):
            if r<0 or r >= len(grid) or c<0 or c>= len(grid[0]) \
                or grid[r][c] != '1':
                return
            
            grid[r][c] = '#'
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(r+dr,c+dc)
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1
        
        return count
                        
class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


        
class Solution4:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        BFS
        '''
        if not grid:
            return 0
        
        def bfs(r,c):
            
            q = collections.deque()
            q.append((r,c))
            
            while q:
                i, j = q.pop()
                for dr, dc in [(1,0),(0,1),(-1,0), (0,-1)]:
                    nr, nc = i + dr, j + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) \
                            or visited[nr][nc] or grid[nr][nc] == '0':
                        continue
                    else:
                        visited[nr][nc] = True
                        q.append((nr,nc))
        
        
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not visited[r][c] and grid[r][c] == '1':
                    bfs(r,c)
                    count += 1
        
        return count




# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2(),Solution3(),Solution4()]:
            func = Sol.numIslands
            self.assertEqual(func([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), 1)
            self.assertEqual(func([["1","1","1","1","0"],["1","1","0","1","0"],["0","0","1","0","0"],["0","0","0","1","1"]]), 3)

if __name__ == '__main__':
    unittest.main()