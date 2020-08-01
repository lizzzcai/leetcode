'''
31/07/2020

140. Word Break II - Hard

Tag: Dynamic Programming, Backtracking

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

'''

from typing import List
# Solution
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        https://leetcode.com/problems/word-break-ii/discuss/44167/My-concise-JAVA-solution-based-on-memorized-DFS
        time: (N^(S/N))
        '''
        def dfs(s, memo):
            if s in memo:
                return memo[s]
            
            res = []
            for w in wordDict:
                if s[:len(w)] == w:
                    sub_res = dfs(s[len(w):], memo)
                    for sub in sub_res:
                        tmp = w
                        if len(sub) > 0:
                            tmp += " " + sub
                        res.append(tmp)
            
            memo[s] = res
            return res
        
        
        memo = {"":[""]}
        return dfs(s, memo)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.wordBreak
            self.assertEqual(set(func("catsanddog", ["cat", "cats", "and", "sand", "dog"])), set(["cats and dog", "cat sand dog"]))
            self.assertEqual(set(func("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])), set(["pine apple pen apple", "pineapple pen apple","pine applepen apple"]))
            self.assertEqual(set(func("catsandog", ["cats", "dog", "sand", "and", "cat"])), set([]))


if __name__ == '__main__':
    unittest.main()