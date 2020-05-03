'''
03/05/2020

1092. Shortest Common Supersequence - Hard

Tag: Dynamic Programming

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.

'''

import collections
from typing import List
# Solution
class Solution1:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        LCS
        https://leetcode.com/problems/shortest-common-supersequence/discuss/312710/C%2B%2BPython-Find-the-LCS
        Time: O(mn)
        Space: O(mn)
        '''
        def lcs(str1, str2):
            n, m = len(str1), len(str2)
            dp = [['']*(m+1) for _ in range(n+1)]
            
            for i in range(n):
                for j in range(m):
                    if str1[i] == str2[j]:
                        dp[i+1][j+1] = dp[i][j] + str1[i]
                    else:
                        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)
            
            return dp[n][m]
        
        lcs = lcs(str1,str2)
        i, j = 0, 0
        res = ""
        
        for c in lcs:
            while str1[i] != c and i < len(str1):
                res += str1[i]
                i += 1
            while str2[j] != c and j < len(str2):
                res += str2[j]
                j += 1
            
            res += c
            i += 1
            j += 1
            
        if i < len(str1):
            res += str1[i:]
            
        if j < len(str2):
            res += str2[j:]
            
        return res


class Solution2:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        LCS
        https://leetcode.com/problems/shortest-common-supersequence/discuss/312757/JavaPython-3-O(mn)-clean-DP-code-w-picture-comments-and-analysis.
        Time: O(mn)
        Space: O(mn)
        '''

        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i, c in enumerate(str1):
            for j, d in enumerate(str2):
                dp[i+1][j+1] = 1 + dp[i][j] if c == d else max(dp[i+1][j], dp[i][j+1])
        
        print(dp)
        i, j = m-1, n-1
        seq = []
        while i >= 0 and j >= 0:
            if str1[i] == str2[j]:
                seq.append(str1[i])
                i -= 1
                j -= 1
            elif dp[i+1][j] < dp[i][j+1]:
                seq.append(str1[i])
                i -= 1
            else:
                seq.append(str2[j])
                j -= 1
            
        return str1[:i+1] + str2[:j+1] + ''.join(reversed(seq))

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.shortestCommonSupersequence
            self.assertEqual(func("abac", "cab"), "cabac")
            self.assertEqual(func("bbbaaaba", "bbababbb"), "bbabaaababb")


if __name__ == '__main__':
    unittest.main()