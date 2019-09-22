"""
21/09/2019
289. Game of Life - Medium
Tag: Array, in-place


According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

"""

from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
        1. use a copy of the board to check the state of the original cell.
        1. to not usinga borad to record the orignal state, we can use some other valoue to reflect the orginal state. if the original state is 1 but now become 0, we assign it as -1. if the original state is 0 but now become 1, we assign it as 2.
        2. iterate throgh the cell one by one, then check it's neighbors, calculate the number of live cell.
        3. apply the rule on this cell and update it's state on the board, based on new rule.
        4. iterate again the board to assign 1, 2 as 1 , 0, -1 as 0
        
        Time Complexity: O(m x n)
        Space Compexity: O(1)
        
        """
        
        n_row = len(board)
        n_col = len(board[0])

        # 8neighbors
        neighbors = [(-1,-1),(-1,0), (-1,1),
                     (0, -1), (0, 1),
                     (1,-1), (1,0), (1,1)]
        # iterate all the cell and check their neighbord
        for r in range(n_row):
            for c in range(n_col):
                # count how many live cell in neighbors
                n_live = 0
                # iterate the neighbors
                for i, j in neighbors:
                    # position of the neighbor
                    n_r = r + i
                    n_c = c + j
                    # check if neighbor inside the board, and check if it's a live cell in the record board.
                    # if it is neighbor and live cell, add one to the count
                    if (0<=n_r<=n_row-1) and (0<=n_c<= n_col-1) and (board[n_r][n_c] == 1 or board[n_r][n_c] == -1):
                        n_live += 1
                
                # apply the rule, update to the the new value by the rule we propose.
                
                # rule 1 & rule 3
                if (board[r][c] == 1) and (n_live < 2 or n_live > 3):
                    board[r][c] = -1
                # rule 2
                # elif record[r][c] == 1 and (2<=n_live<=3):
                #   board[r][c] = 1

                # rule 4
                if board[r][c] == 0 and n_live == 3:
                    board[r][c] = 2
                    
        # iterate again to convert 2 as 1 and -1 as 0
        for r in range(n_row):
            for c in range(n_col):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

        return board
                
        

# Unit Test
import unittest
class gameOfLifeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gameOfLife(self):
        func = Solution().gameOfLife

        self.assertEqual(func([[0,1,0],
                            [0,0,1],
                            [1,1,1],
                            [0,0,0]]), [
                                        [0,0,0],
                                        [1,0,1],
                                        [0,1,1],
                                        [0,1,0]
                                        ])






if __name__ == '__main__':
    unittest.main()


