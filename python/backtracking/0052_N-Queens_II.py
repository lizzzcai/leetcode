'''
26/03/2020

52. N-Queens II - Hard

Tag: Backtracking

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''

from typing import List
# Solution
class Solution1:
    def totalNQueens(self, n: int) -> int:
        
        def is_valid(board, row, col):
            # check upper
            r = row-1
            while r >= 0:
                if board[r][col] == 'Q':
                    return False
                r -= 1
                
            # check up left
            r, c = row-1, col-1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            
            # check up right
            r, c = row-1, col+1
            while r >= 0 and c < len(board[0]):
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
                
            return True
    
    
        def backtrack(board, row):
            if row == len(board):
                return 1
            
            out = 0
            for col in range(len(board[0])):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    out += backtrack(board, row+1)
                    board[row][col] = '.'
            return out

        board = [['.' for _ in range(n)] for _ in range(n)]
        res = backtrack(board, 0)
        return res

class Solution2:
    def totalNQueens(self, n: int) -> int:
        
        def is_valid(board, row):
            # check if queen in same colum or diagonal
            for i in range(row):
                if board[i] == board[row] or abs(board[i]-board[row]) == row-i:
                    return False
                
            return True
    
    
        def backtrack(board, row):
            if row == len(board):
                return 1
            
            out = 0
            for col in range(len(board)):
                board[row] = col
                if is_valid(board, row):
                    out += backtrack(board, row+1)
            return out

        board = [-1]*n
        res = backtrack(board, 0)
        return res
        
        
class Solution3:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(n, row):
            if row == n:
                return 1
            
            out = 0
            for col in range(n):
                if col not in cols and row-col not in diags and row+col not in off_diags:
                    cols.append(col)
                    diags.append(row-col)
                    off_diags.append(row+col)
                    out += backtrack(n, row+1)
                    cols.pop()
                    diags.pop()
                    off_diags.pop()
            return out

        cols = []
        diags = []
        off_diags = []
        res = backtrack(n, 0)
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2(),Solution3()]:
            func = Sol.totalNQueens
            out = [
                    [".Q..",
                    "...Q",
                    "Q...",
                    "..Q."],
                     ["..Q.",
                    "Q...",
                    "...Q",
                    ".Q.."]
                ]
            self.assertEqual(func(4), 2)

if __name__ == '__main__':
    unittest.main()