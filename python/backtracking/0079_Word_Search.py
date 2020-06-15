'''
14/06/2020

79. Word Search - Medium

Tag: Array, Backtracking

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        
        # start to find word in i, j
        def dfs(i, j, idx, visited):
            if idx == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx] or (i, j) in visited:
                return False
            
            visited.append((i, j))
            res = any([dfs(i+di,j+dj,idx+1,visited) for di, dj in dirs])
            if not res:
                visited.pop()
            return res
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, []):
                    return True
        return False
            

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.exist
            self.assertEqual(func([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True)
            self.assertEqual(func([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), True)
            self.assertEqual(func([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"), False)


if __name__ == '__main__':
    unittest.main()