'''
08/05/2020

211. Add and Search Word - Data structure design - Medium

Tag: Design, Tire, Backtracking

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''
import collections
from typing import List
# Solution
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        nodes = self.next
        for ch in word:
            if ch not in nodes:
                nodes[ch] = {}
            nodes = nodes[ch]
        nodes['#'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(word, nodes):
            if not word:
                return '#' in nodes
            
            
            if word[0] in nodes:
                return dfs(word[1:], nodes[word[0]])
            elif word[0] == '.':
                return any(dfs(word[1:], nodes[c]) for c in nodes if c != '#')
            else:
                return False
            
        return dfs(word, self.next)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [WordDictionary]:
            func = Sol()
            func.addWord('bad')
            func.addWord('dad')
            func.addWord('mad')
            self.assertEqual(func.search("pad"), False)
            self.assertEqual(func.search("bad"), True)
            self.assertEqual(func.search(".ad"), True)
            self.assertEqual(func.search("b.."), True)

if __name__ == '__main__':
    unittest.main()