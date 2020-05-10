'''
10/05/2020

745. Prefix and Suffix Search - Hard

Tag: Trie

Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
 

Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
 

'''

from typing import List
# Solution
class Tire:
    def __init__(self):
        self.next = {}
        
    def insert_root(self, word):
        nodes = self.next
        for ch in word:
            if ch not in nodes:
                nodes[ch] = {}
            nodes = nodes[ch]
        
        nodes['#'] = True
    
    def find_root(self, word):
        nodes = self.next
        for idx, ch in enumerate(word):
            if ch not in nodes:
                return word
            nodes = nodes[ch]
            if '#' in nodes:
                return word[:idx+1]
        return word
            
            
class WordFilter1:

    def __init__(self, words: List[str]):
        '''
        https://leetcode.com/problems/prefix-and-suffix-search/discuss/110053/Python-few-ways-to-do-it-with-EXPLANATIONS!-U0001f389
        '''
        self.dic = {}
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                for j in range(len(word)+1):
                    self.dic[word[:i]+"#"+word[j:]] = weight
        
    def f(self, prefix: str, suffix: str) -> int:
        
        return self.dic.get(f'{prefix}#{suffix}', -1)
    

class WordFilter2:
    '''
    Trie of Suffix Wrapped Words
    Time: O(NK^2+QK)
    Space O(NK^2)
    https://leetcode.com/problems/prefix-and-suffix-search/discuss/144432/Java-Beat-95-just-small-modifications-in-implementing-Trie.
    '''
    def __init__(self, words: List[str]):
        self.next = {}
        for weight, word in enumerate(words):
            word = '#' + word
            self.__add_word(self.next, word, weight)
            for i in range(len(word)):
                self.__add_word(self.next, word[i+1:]+word, weight)
                    
    def __add_word(self, next, word, weight):
        nodes = next
        for ch in word:
            if ch not in nodes:
                nodes[ch] = {}
            nodes = nodes[ch]
            nodes['$'] = weight

    def f(self, prefix: str, suffix: str) -> int:
        curr = self.next
        for letter in suffix + '#' + prefix:
            if letter not in curr:
                return -1
            curr = curr[letter]
        return curr['$']
        
    

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [WordFilter1, WordFilter2]:
            func = Sol(["apple"])
            self.assertEqual(func.f('a', 'e'), 0)
            self.assertEqual(func.f('b', ''), -1)

if __name__ == '__main__':
    unittest.main()