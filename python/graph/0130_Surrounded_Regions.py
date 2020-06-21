'''
09/01/2020

130. Surrounded Regions - Medium

Tag: BFS

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

from typing import List
from collections import deque
# Solution 0
class Solution0:
    '''
    Time complexity : O(MXN)
    Space complexity : O(1)

    First, check the four border of the matrix. If there is a element is
    'O', alter it and all its neighbor 'O' elements to 'N'.

    Then ,alter all the 'O' to 'X'

    At last,alter all the 'N' to 'O'

    example: 

    X X X X           X X X X             X X X X
    X X O X  ->       X X O X    ->       X X X X
    X O X X           X N X X             X O X X
    X O X X           X N X X             X O X X

    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return
        
        # queue for bfs
        q = deque()
        
        # start from the boarder and replace all O to N
        # put all the boarder value into queue.
        for r in range(R):
            q.append((r, 0))
            q.append((r, C-1))

        for c in range(C):
            q.append((0, c))
            q.append((R-1, c))
        
        while q:
            r, c = q.popleft()
            if 0<=r<R and 0<=c<C and board[r][c] == "O":
                # modify the value from O to N
                board[r][c] = "N"
                # append the surrouding cells to queue.
                q.append((r, c+1))
                q.append((r, c-1))
                q.append((r-1, c))
                q.append((r+1, c))
        
        # replace all the O to X, then replace all the N to O
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"

        # for easy verify            
        return board

class Solution1:

    '''
    recursion, dfs
    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return
        
        # start from the boarder and replace all O to N
        # put all the boarder value into queue.
        for r in range(R):
            self.dfs(board, r, 0, R, C)
            self.dfs(board, r, C-1, R, C)

        for c in range(C):
            self.dfs(board, 0, c, R, C)
            self.dfs(board, R-1, c, R, C)

        # replace all the O to X, then replace all the N to O
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"
        
        return board
                    
    def dfs(self, board, r, c, R, C):
        if 0<=r<R and 0<=c<C and board[r][c] == "O":
            board[r][c] = "N"
            self.dfs(board, r, c+1, R, C)
            self.dfs(board, r, c-1, R, C)            
            self.dfs(board, r-1, c, R, C)            
            self.dfs(board, r+1, c, R, C)   
    
class DSU:
    def __init__(self):
        self.par = {}
        
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def _add(self, x):
        if x in self.par:
            return
        self.par[x] = x
    
    def union(self, x, y):
        if x not in self.par:
            self._add(x)
        if y not in self.par:
            self._add(y)
        
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        
        self.par[xr] = yr
        return True
    
    def is_connected(self, x, y):
        if x not in self.par:
            self._add(x)
        if y not in self.par:
            self._add(y)
        
        xr, yr = self.find(x), self.find(y)
        return xr == yr

    
class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return
        
        dsu = DSU()
        for r in range(0, R):
            for c in range(0, C):
                # start from the boarder and connect all 'O' to dummy node R*C
                if board[r][c] == 'O' and (r == 0 or c == 0 or r == R-1 or c == C-1):
                    dsu.union(r*R+c, R*C)
                elif board[r][c] == 'O':
                    # if the middle is 'O' and the cell in 4 dirs is 'O', connect together
                    for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nr, nc = r+dr, c+dc
                        if board[nr][nc] == 'O':
                            dsu.union(r*R+c, nr*R+nc)
        
        # check if the cell is connected to the dummy node
        for r in range(R):
            for c in range(C):
                if not dsu.is_connected(r*R+c, R*C):
                    board[r][c] = 'X'

        return board
        
        
        

# Unit Test
import unittest
class solveCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solveCase(self):
        func = Solution0().solve
        self.assertEqual(func([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]), [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])

        func = Solution1().solve
        self.assertEqual(func([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]), [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])

        func = Solution2().solve
        self.assertEqual(func([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]), [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])


if __name__ == '__main__':
    unittest.main()