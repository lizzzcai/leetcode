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


class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Time:O(N!)
        Space: O(N)
        
        '''
        def is_valid(board, row):
            for i in range(row):
                # check if queen in same colum or diagonal
                if board[i] == board[row] or abs(board[i]-board[row]) == row-i:
                    return False
            return True

    
        def backtrack(board, row):
            # terminate if row reach the end
            if row == len(board):
                tmp = "."*len(board)
                res.append([tmp[:i]+"Q"+tmp[i+1:] for i in board])
                return
            
            for col in range(len(board)):
                # make selection, each col in ROW
                board[row] = col
                # if valid, no two queens attach each other
                if is_valid(board, row):
                    # go to next row
                    backtrack(board, row + 1)

            
        board = [-1]*n
        res = []
        backtrack(board, 0)
        return res


class Solution3:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Time:O(N!)
        Space: O(N)
        
        
            diags (row_idx - col_idx):
            3 |  3  2  1  0
            2 |  2  1  0 -1
            1 |  1  0 -1 -2
            0 |  0 -1 -2 -3
            r  ------------
              c  0  1  2  3

            off_diags (row_idx + col_idx):
            3 |  3  4  5  6
            2 |  2  3  4  5
            1 |  1  2  3  4
            0 |  0  1  2  3
            r  ------------
              c  0  1  2  3
        '''
        def backtrack(board, row):
            # terminate if row reach the end
            if row == len(board):
                res.append([tmp[:i]+"Q"+tmp[i+1:] for i in board])
                return
            
            for col in range(len(board)):
                # make selection, each col in ROW
                board[row] = col
                # check if no two queens on the rows or diags
                if col not in cols and row-col not in diags and row+col not in off_diags:
                    # go to next row
                    cols.append(col)
                    diags.append(row-col)
                    off_diags.append(row+col)
                    backtrack(board, row + 1)
                    cols.pop()
                    diags.pop()
                    off_diags.pop()

            
        board = [-1]*n
        tmp = "."*len(board)
        cols = []
        diags = []
        off_diags = []
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
        for Sol in [Solution1(), Solution2(), Solution3()]:
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