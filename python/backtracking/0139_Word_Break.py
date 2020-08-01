'''
31/07/2020

139. Word Break - Medium

Tag: Dynamic Programming

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''

from typing import List
# Solution
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(s, wordDict, memo):
            
            if s in memo:
                return memo[s]
            
            res = []
            for w in wordDict:
                n = len(w)
                if len(s) >= n and s[:n] == w:
                    res.append(dfs(s[n:], wordDict, memo))
            
            memo[s] = any(res)
            return memo[s]
        
        memo = {"":True}
        return dfs(s, wordDict, memo)



class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        DP
        time: O(n^2)
        '''
        
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        
        wordSet = set(wordDict)
        
        for j in range(1, n+1):
            for w in wordSet:
                l = len(w)
                if dp[j-l] and s[j-l:j] in wordSet:
                    dp[j] = True
                    break
        
        return dp[n]
                

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.wordBreak
            self.assertEqual(func("leetcode", ["leet", "code"]), True)
            self.assertEqual(func("applepenapple", ["apple", "pen"]), True)
            self.assertEqual(func("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)


if __name__ == '__main__':
    unittest.main()