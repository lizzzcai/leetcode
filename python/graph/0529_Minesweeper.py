'''
09/01/2020

529. Minesweeper - Medium

Tag: DFS

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

 

Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

'''

from typing import List
# Solution
class Solution:
    '''
    DFS solution

    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # get the number of rows and cols
        R, C = len(board), len(board[0])
        # first click
        r, c = click[0], click[1]
        
        def dfs(r, c):
            # if its a unrevealed empty square
            if board[r][c] == 'E':
                count = 0
                # explore the adjacent cells
                for dr, dc in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                    i, j = r+dr, c+dc
                    # if in board and its a mine, add count
                    if 0<=i<R and 0<=j<C and board[i][j]=='M':
                        count += 1
                # rule 3
                if count > 0:
                    board[r][c] = str(count)
                else: 
                    # rule 2
                    board[r][c] = 'B'
                    # all of its adjacent unrevealed squares should be revealed recursively
                    for dr, dc in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                        i, j = r+dr, c+dc
                        if 0<=i<R and 0<=j<C:
                            dfs(i,j)
        
        # rule one
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)
            
        return board


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().updateBoard
        self.assertEqual(func([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [3,0]), [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]])

if __name__ == '__main__':
    unittest.main()