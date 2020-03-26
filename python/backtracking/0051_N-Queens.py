'''
26/03/2020

51. N-Queens - Hard

Tag: Backtracking

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

'''

from typing import List
# Solution
class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # if can put queen in board[row][col]
        def is_valid(board, row, col):
            # check upper
            i = row-1
            while i >= 0:
                if board[i][col] == 'Q':
                    return False
                i -= 1
            
            # check up left
            i, j = row-1, col-1
            while i >=0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # check up right
            i, j = row-1, col+1
            while i >=0 and j < len(board[0]):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

    
        def backtrack(board, row):
            # terminate if row reach the end
            if row == len(board):
                res.append([''.join(row) for row in board])
                return
            
            for c in range(len(board[0])):
                # if valid, no two queens attach each other
                if is_valid(board, row, c):
                    # make selection, each col in ROW
                    board[row][c] = 'Q'
                    # go to next row
                    backtrack(board, row + 1)
                    # revoke selection
                    board[row][c] = '.'
            
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        backtrack(board, 0)
        return res





# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.solveNQueens
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
            self.assertEqual(set(tuple(x) for x in func(4)), set(tuple(x) for x in out))

if __name__ == '__main__':
    unittest.main()