'''
07/05/2020

676. Implement Magic Dictionary - Medium

Tag: Hash Table, Tire

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

'''
import collections
from typing import List
# Solution
class MagicDictionary1:
    '''
    O(sum(wi^2)) to build, O(K^2) to search
    Space: O(sum(wi^2))
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.words = {}
        
    def __candidates(self, word):
        for i in range(len(word)):
            yield word[:i]+'*'+word[i+1:]
        
    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.words = set(dict)
        self.count = collections.Counter(cand for word in dict for cand in self.__candidates(word))


    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return any(self.count[cand] > 1 or self.count[cand] == 1 and word not in self.words for cand in self.__candidates(word))



class MagicDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = {}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.__insert(word)
    
    def __insert(self, word):
        nodes = self.next
        for ch in word:
            if ch not in nodes:
                nodes[ch] = {}
            nodes = nodes[ch]
        nodes['#'] = len(word)
        
        
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        def dfs(remain, word, nodes):
            if remain < 0 or not word:
                return remain == 0 and "#" in nodes
            

            return any(dfs(remain-(c!=word[0]), word[1:], nodes[c]) for c in nodes if c != '#')
        
        res = dfs(1, word, self.next)
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [MagicDictionary1, MagicDictionary2]:
            func = Sol()
            dict = ["hello", "leetcode"]
            func.buildDict(dict)
            self.assertEqual(func.search("hello"), False)
            self.assertEqual(func.search("hhllo"), True)
            self.assertEqual(func.search("hell"), False)
            self.assertEqual(func.search("leetcoded"), False)

if __name__ == '__main__':
    unittest.main()