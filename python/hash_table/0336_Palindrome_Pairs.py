'''
07/05/2020

336. Palindrome Pairs - Hard

Tag: Hash Table, String, Trie

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n^2*K)
    Space complexity : O(n^2)
    '''
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def check(s):
            i, j = 0, len(s)-1
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            
            return True
                
        
        n = len(words)
        res = []
        for i in range(n-1):
            s1 = words[i]
            for j in range(i+1, n):
                s2 = words[j]
                if s1 and s2:
                    if s1[0] == s2[-1] and check(s1+s2):
                        res.append([i,j])
                    if s1[-1] == s2[0] and check(s2+s1):
                        res.append([j,i])
                else:
                    if check(s1) and check(s2):
                        res.append([i,j])
                        res.append([j,i])
        
        return res


class Solution2:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        '''
        https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
        Time: O(n*K^2)
        Space: O(n)
        
        '''
        def is_palindrome(s):
            return s == s[::-1]
        
        lookup = {w:idx for idx,w in enumerate(words)}
        
        res = []
        for word, idx in lookup.items():
            for j in range(len(word)+1):
                prefix = word[:j]
                suffix = word[j:]
                
                if is_palindrome(prefix):
                    suffix_r = suffix[::-1]
                    # aviod cause when j = 0 and the word is self-palindrome
                    if suffix_r in lookup and lookup[suffix_r] != idx:
                        res.append([lookup[suffix_r], idx])
                
                # j != len(word) to avoid duplicate case as it was done when j = 0 in prefix
                if j != len(word) and is_palindrome(suffix):
                    prefix_r = prefix[::-1]
                    #if prefix_r in lookup:
                    if prefix_r in lookup and lookup[prefix_r] != idx:
                        res.append([idx, lookup[prefix_r]])
        
        return res
                
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.palindromePairs
            self.assertEqual(func(["abcd","dcba","lls","s","sssll"]), [[0,1],[1,0],[3,2],[2,4]])
            self.assertEqual(func(["bat","tab","cat"]), [[0,1],[1,0]])
            self.assertEqual(func(["bat","tab",""]), [[0,1],[1,0]])
            self.assertEqual(func([]), [])
            self.assertEqual(func(["a",""]), [[0,1],[1,0]])
if __name__ == '__main__':
    unittest.main()