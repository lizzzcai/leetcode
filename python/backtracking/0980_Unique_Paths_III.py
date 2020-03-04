'''
04/03/2020

980. Unique Paths III - Hard

Tag: Backtracking, DFS

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20

'''

from typing import List
# Solution
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        '''
        Time: O(4^(R*C))
        Space: O(1)
        
        '''
        def dfs(r, c, step):
            if r < 0 or r > rows-1 or c < 0 or c > cols-1 or grid[r][c] == -1 or step < 0:
                return

            if grid[r][c] == 2:
                if step == 0:
                    self.res += 1
                return
            
            # set the current grid to -1 to block it
            grid[r][c] = -1
            for d in directs:
                dfs(r+d[0], c+d[1], step-1)
            # set the current grid to 0 to unblock it
            grid[r][c] = 0
        
        
        start_r, start_c = 0, 0
        steps = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # 4 direction walks
        directs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # find the start point and number of empty squares
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 0:
                    steps += 1
        #add one as last step is to the end square.
        steps += 1
        # number of walks
        self.res = 0
        dfs(start_r, start_c, steps)
        
        return self.res


class Solution1:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        '''
        Time: O(4^(R*C))
        Space: O(1)
        
        '''
        def dfs(r, c, step):
            if r < 0 or r > rows-1 or c < 0 or c > cols-1 or grid[r][c] == -1 or step < 0:
                return 0

            if grid[r][c] == 2:
                if step == 0:
                    return 1
                return 0
            
            res = 0
            # set the current grid to -1 to block it
            grid[r][c] = -1
            for d in directs:
                res += dfs(r+d[0], c+d[1], step-1)
            # set the current grid to 0 to unblock it
            grid[r][c] = 0
            
            return res
        
        
        start_r, start_c = 0, 0
        steps = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # 4 direction walks
        directs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # find the start point and number of empty squares
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 0:
                    steps += 1
        #add one as last step is to the end square.
        steps += 1
        # number of walks
        ans = dfs(start_r, start_c, steps)
        
        return ans

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().uniquePathsIII
        self.assertEqual(func([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]), 2)
        self.assertEqual(func([[1,0,0,0],[0,0,0,0],[0,0,0,2]]), 4)
        self.assertEqual(func([[0,1],[2,0]]), 0)

        


if __name__ == '__main__':
    unittest.main()