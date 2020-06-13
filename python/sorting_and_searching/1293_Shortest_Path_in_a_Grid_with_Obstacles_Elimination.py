'''
13/06/2020

1293. Shortest Path in a Grid with Obstacles Elimination - Hard

Tag: BFS

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0

'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    BFS
    Time complexity : O(nm)
    Space complexity : O(nm)
    '''
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        if R == 1 and C == 1:
            return 0
    
        # r, c, remaining k, steps
        queue = collections.deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        if k >= R-1+C-1:
            return R-1+C-1
        
        while queue:
            r, c, remain, step = queue.popleft()
            for dr, dc in dirs:
                if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]):
                    if grid[r+dr][c+dc] == 0 and (r+dr,c+dc, remain) not in visited:
                        queue.append((r+dr,c+dc, remain, step+1))
                        visited.add((r+dr,c+dc, remain))
                    elif grid[r+dr][c+dc] == 1 and remain > 0 and (r+dr,c+dc, remain-1) not in visited:
                        queue.append((r+dr,c+dc, remain-1, step+1))
                        visited.add((r+dr,c+dc, remain-1))
                    
                    if r+dr == len(grid)-1 and c+dc == len(grid[0])-1:
                        return step+1
        
        return -1

class Solution2:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        if R == 1 and C == 1:
            return 0
    
        # r, c, remaining k, steps
        queue = collections.deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        if k >= R-1+C-1:
            return R-1+C-1
        
        while queue:
            r, c, remain, step = queue.popleft()
            for dr, dc in dirs:
                if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]):
                    state = remain - grid[r+dr][c+dc]
                    if (r+dr,c+dc, state) not in visited and state>=0:
                        queue.append((r+dr,c+dc, state, step+1))
                        visited.add((r+dr,c+dc, state))
                    
                    if r+dr == len(grid)-1 and c+dc == len(grid[0])-1:
                        return step+1
                 
        return -1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.shortestPath
            self.assertEqual(func([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1), 6)
            self.assertEqual(func([[0,1,1],[1,1,1],[1,0,0]], 1), -1)



if __name__ == '__main__':
    unittest.main()