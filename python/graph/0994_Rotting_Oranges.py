'''
19/05/2020

994. Rotting Oranges - Medium

Tag: BFS

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = collections.deque()
        num_fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    num_fresh += 1
        
        if num_fresh == 0:
            return 0
        steps = 0
        dirs = [(1,0), (0,1),(-1,0),(0,-1)]
        
        while queue:
            n = len(queue)
            for _ in range(n):
                r,c = queue.popleft()
                for dr, dc in dirs:
                    if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        num_fresh -= 1
                        queue.append((r+dr,c+dc))
                        
            steps+=1
            if num_fresh == 0:
                return steps
        
        return steps if num_fresh == 0 else -1


class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = set()
        rotting = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotting.add((r,c))
                elif grid[r][c] == 1:
                    fresh.add((r,c))
        
        steps = 0
        dirs = [(1,0), (0,1),(-1,0),(0,-1)]
        
        while fresh:
            if not rotting:
                return -1
            rotting1 = set()
            for r, c in rotting:
                for dr, dc in dirs:
                    if (r+dr,c+dc) in fresh:
                        rotting1.add((r+dr,c+dc))
            
            fresh -= rotting1
            rotting = rotting1
            steps += 1
            
        return steps
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.orangesRotting
            self.assertEqual(func([[2,1,1],[1,1,0],[0,1,1]]), 4)
            self.assertEqual(func([[2,1,1],[0,1,1],[1,0,1]]), -1)
            self.assertEqual(func([[0,2]]), 0)



if __name__ == '__main__':
    unittest.main()