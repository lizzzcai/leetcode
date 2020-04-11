'''
11/04/2020

1391. Check if There is a Valid Path in a Grid - Medium

Tag: Depth-first Search, Breadth-first Search

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

from typing import List
# Solution
class Solution1:
    '''
    dfs
    Time complexity : O(nm)
    Space complexity : O(nm)
    '''
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        hmap = {
            1:{(1,0):[], (0,1):[1,3,5], (-1,0):[], (0,-1):[1,4,6]},
            2:{(1,0):[2,5,6], (0,1):[], (-1,0):[2,3,4], (0,-1):[]},
            3:{(1,0):[2,5,6], (0,1):[], (-1,0):[], (0,-1):[1,4,6]},
            4:{(1,0):[2,5,6], (0,1):[1,3,5], (-1,0):[], (0,-1):[]},
            5:{(1,0):[], (0,1):[], (-1,0):[2,3,4], (0,-1):[1,4,6]},
            6:{(1,0):[], (0,1):[1,3,5], (-1,0):[2,3,4], (0,-1):[]}
        }

        
        visited = set()
        def dfs(grid, visited, r,c):
            if r == len(grid)-1 and c == len(grid[0])-1:
                return True
            
            visited.add((r,c))
            choose_set = hmap[grid[r][c]]
            for d, choose in choose_set.items():
                i, j = r+d[0], c+d[1]
                if 0<=i<=len(grid)-1 and 0<=j<= len(grid[0])-1 and (i,j) not in visited and grid[i][j] in choose:
                    return dfs(grid, visited, i,j)
            
            return False
        
        return dfs(grid, visited, 0, 0)


class Solution2:
    '''
    bfs
    Time complexity : O(nm)
    Space complexity : O(nm)
    '''
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        hmap = {
            1:{(1,0):[], (0,1):[1,3,5], (-1,0):[], (0,-1):[1,4,6]},
            2:{(1,0):[2,5,6], (0,1):[], (-1,0):[2,3,4], (0,-1):[]},
            3:{(1,0):[2,5,6], (0,1):[], (-1,0):[], (0,-1):[1,4,6]},
            4:{(1,0):[2,5,6], (0,1):[1,3,5], (-1,0):[], (0,-1):[]},
            5:{(1,0):[], (0,1):[], (-1,0):[2,3,4], (0,-1):[1,4,6]},
            6:{(1,0):[], (0,1):[1,3,5], (-1,0):[2,3,4], (0,-1):[]}
        }
        
        memo = set()
        def bfs(grid, memo, r,c):
            stack = [(0,0)]
            while stack:
                r,c = stack.pop()
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return True
                memo.add((r,c))
                choose_set = hmap[grid[r][c]]
                for d, choose in choose_set.items():
                    i, j = r+d[0], c+d[1]
                    if 0<=i<=len(grid)-1 and 0<=j<= len(grid[0])-1 and (i,j) not in memo and grid[i][j] in choose:
                        stack.append((i,j))

            return False
        
        return bfs(grid, memo, 0, 0)


class Solution3:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs = {
            1:[(0,1),(0,-1)],
            2:[(1,0),(-1,0)],
            3:[(1,0),(0,-1)],
            4:[(1,0),(0,1)],
            5:[(-1,0),(0,-1)],
            6:[(0,1),(-1,0)]
        }
        
        visited = set()
        def dfs(grid, visited, r,c):
            if r == len(grid)-1 and c == len(grid[0])-1:
                return True
            
            visited.add((r,c))
            for d in dirs[grid[r][c]]:
                i, j = r+d[0], c+d[1]
                # (-d[0],-d[1]) in dirs[grid[i][j]]
                #When traversing from one cell to the next. the next cell must have a direction that is the opposite of the direction we are moving in for the cells to be connected. For example, if we are moving one unit to the right, then from the next cell it must be possible to go one unit to the left, otherwise it's not actually connected.
                if 0<=i<=len(grid)-1 and 0<=j<= len(grid[0])-1 and (i,j) not in visited and (-d[0],-d[1]) in dirs[grid[i][j]]:
                    return dfs(grid, visited, i,j)
            
            return False
        
        return dfs(grid, visited, 0, 0)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.hasValidPath
            self.assertEqual(func([[2,4,3],[6,5,2]]), True)
            self.assertEqual(func([[1,2,1],[1,2,1]]), False)
            self.assertEqual(func([[1,1,2]]), False)
            self.assertEqual(func([[1,1,1,1,1,1,3]]), True)
            self.assertEqual(func([[2],[2],[2],[2],[2],[2],[6]]), True)

if __name__ == '__main__':
    unittest.main()