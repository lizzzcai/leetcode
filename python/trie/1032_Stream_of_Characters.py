'''
26/08/2020

1032. Stream of Characters - Hard

Tag: Trie

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.

'''

from typing import List
import collections
# Solution
class StreamChecker:
    '''
    Time complexity : O(QW)
    Space complexity : O(W)
    '''

    def __init__(self, words: List[str]):
        self.tire_reverse = {}
        self.max_size = 0
        for w in words:
            self._insert_reverse(w[::-1])
            self.max_size = max(self.max_size, len(w))
        
        self.q = collections.deque([])

    def _insert_reverse(self, word):
        curr = self.tire_reverse
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['$'] = True
        
    def _search(self, w):
        curr = self.tire_reverse
        for c in w:
            if c in curr:
                curr = curr[c]
                if '$' in curr:
                    return True
            else:
                break
        
        return False

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        if len(self.q) > self.max_size:
            self.q.pop()

        return self._search(self.q)




# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [StreamChecker]:
            func = Sol(["cd","f","kl"])
            self.assertEqual(func.query('a'), False)
            self.assertEqual(func.query('b'), False)
            self.assertEqual(func.query('c'), False)
            self.assertEqual(func.query('d'), True)

            self.assertEqual(func.query('e'), False)
            self.assertEqual(func.query('f'), True)

            self.assertEqual(func.query('g'), False)
            self.assertEqual(func.query('h'), False)
            self.assertEqual(func.query('i'), False)
            self.assertEqual(func.query('j'), False)
            self.assertEqual(func.query('k'), False)
            self.assertEqual(func.query('l'), True)




if __name__ == '__main__':
    unittest.main()