'''
03/07/2020

212. Word Search II - Easy

Tag: Tire, Backtracking

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

'''

from typing import List

class Trie():
    def __init__(self):
        self.tire = {}
    
    def insert(self, word):
        node = self.tire
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['#'] = True
    
    def search(self, word):
        node = self.tire
        for w in word:
            if w not in node:
                return False
            node = node[w]        
        return '#' in node

    
class Solution1:
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.tire
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if '#' in node:
            res.append(path)
            node.pop('#')
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        tmp = board[i][j]
        if tmp not in node:
            return
        node = node[tmp]
        board[i][j] = "$"
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            self.dfs(board, node, i+dr, j+dc, path + tmp, res)
        board[i][j] = tmp
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findWords
            self.assertEqual(func([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]), ["oath","eat"])

if __name__ == '__main__':
    unittest.main()