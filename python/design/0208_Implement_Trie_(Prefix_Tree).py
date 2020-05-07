'''
07/05/2020

208. Implement Trie (Prefix Tree) - Hard

Tag: Design, Trie

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

'''

from typing import List
# from __future__ import annotations python 3.7+
# Solution

class Trie1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_end = False
        self.next = [None]*26
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                node.next[idx] = Trie1()
            node = node.next[idx]
        # set is_end of word to True
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                return False
            node = node.next[idx]
        
        return node.is_end == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                return False
            node = node.next[idx]
        return True
            


class Trie2:
    '''
    Create O(N*K)
    Insearch: time: O(L) space: O(L) worse
    Search: time: O(L)
    Space O(m^n), n is the height, m is the size of table

    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_end = False
        self.next = [None]*26
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                node.next[idx] = Trie2()
            node = node.next[idx]
        # set is_end of word to True
        node.is_end = True

    def __search_prefix(self, prefix: str) -> 'Trie':
        """
        Returns Node if the Prefix is in the trie.
        """
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                return None
            node = node.next[idx]
        return node

        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.__search_prefix(word)
        return node != None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.__search_prefix(prefix)
        return node != None



class Trie3:
    '''
    use {} to store the next node

    Create O(N*K)
    Insearch: time: O(L) space: O(L) worse
    Search: time: O(L)
    Space O(m^n), n is the height, m is the size of table

    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.next
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        # set end of word to True
        node['-'] = True

    def __search_prefix(self, prefix: str) -> dict:
        """
        Returns Node if the Prefix is in the trie.
        """
        node = self.next
        for ch in prefix:
            if ch not in node:
                return None
            node = node[ch]
        return node

        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.__search_prefix(word)
        return node != None and '-' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.__search_prefix(prefix)
        return node != None

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Trie1, Trie2, Trie3]:
            func = Sol()
            func.insert("apple")
            self.assertEqual(func.search("apple"), True)
            self.assertEqual(func.search("app"), False)
            self.assertEqual(func.startsWith("app"), True)
            func.insert("app")
            self.assertEqual(func.search("app"), True)

if __name__ == '__main__':
    unittest.main()