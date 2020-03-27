'''
27/03/2020

37. Sudoku Solver - Hard

Tag: Backtracking, Hash Table

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''

from typing import List
# Solution
class Solution1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, n):
            
            for i in range(9):
                # same row
                if board[row][i] == n:
                    return False
                # same col
                if board[i][col] == n:
                    return False
                # 3x3 sub-box
                if board[(row//3)*3+i//3][(col//3)*3+i%3] == n:
                    return False 
                
            return True
        
            
        def backtrack(board, row, col):
            if col == len(board[0]):
                return backtrack(board, row+1, 0)
            if row == len(board):
                self.res = board
                return True
            
            for r in range(row, len(board)):
                for c in range(col, len(board[0])):
                    
                    if board[r][c] != '.':
                        return backtrack(board, r, c+1)
                    
                    for i in range(1, 10):
                        if not is_valid(board, r, c, str(i)):
                            continue
                        board[r][c] = str(i)
                        if(backtrack(board, r, c+1)):
                            return True
                        board[r][c] = '.'
                                
                    return False
            return False

        
        self.res = None
        backtrack(board, 0, 0)
        return self.res


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.solveSudoku
            src = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
            dst = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
            self.assertEqual(set(tuple(x) for x in func(src)), set(tuple(x) for x in dst))

if __name__ == '__main__':
    unittest.main()