"""
27/09/2019
1143. Longest Common Subsequence - Medium
Tag: Dynamic Programming

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""

from typing import List


class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis
        Time O(mn)
        Space O(mn)
        
        '''
        n, m = len(text1), len(text2)
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        check = [[0]*(m+1) for _ in range(n+1)]
        
        def getLCS1(text1, text2, b):
            LCS = ""
            i = len(text1)-1
            j = len(text2)-1
            while i >= 0 and j >= 0:
                if b[i+1][j+1] == "ADDXY":
                    LCS += text1[i]
                    i -= 1
                    j -= 1
                elif b[i+1][j+1] == "SKIPX":
                    i -= 1
                else:
                    j -= 1

            return LCS[::-1]

        def getLCS2(text1, text2, b):
            LCS = ""
            i = len(text1)-1
            j = len(text2)-1
            idx = b[i+1][j+1]
            while i >= 0 and j >= 0 and idx > 0:

                while i >= 0 and b[i][j+1] == idx:
                    i -= 1
                while j >= 0 and b[i+1][j] == idx:
                    j -= 1
                
                LCS = text1[i] + LCS
                i -= 1
                j -= 1
                idx -= 1

            return LCS
            
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                    check[i+1][j+1] = "ADDXY"
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                    if dp[i+1][j] >= dp[i][j+1]:
                        check[i+1][j+1] = "SKIPY"
                    else:
                        check[i+1][j+1] = "SKIPX"
        

        print(text1, text2, getLCS1(text1, text2, check), getLCS2(text1, text2, dp))
        print(dp)
        return dp[-1][-1]
            
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        1-D DP
        https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis
        Time O(mn)
        Space O(m)
        
        '''
        n, m = len(text1), len(text2)
        dp = [0]*(m+1)
        for i in range(n):
            dp1 = [0]*(m+1)
            for j in range(m):
                if text1[i] == text2[j]:
                    dp1[j+1] = 1+dp[j]
                else:
                    dp1[j+1] = max(dp1[j], dp[j+1])
            dp = dp1
        
        return dp[-1]


class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        1-D DP
        https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis
        Time O(mn)
        Space O(min(m, n))
        
        '''
        n, m = len(text1), len(text2)
        if m > n:
            return self.longestCommonSubsequence(text2, text1)
        dp = [0]*(m+1)
        for i in range(n):
            prev_row = 0
            prev_row_col = 0
            for j in range(m):
                prev_row, prev_row_col = dp[j+1], prev_row
                if text1[i] == text2[j]:
                    dp[j+1] = prev_row_col + 1
                else:
                    dp[j+1] = max(dp[j], prev_row)
        
        return dp[-1]

class Solution4:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        def helper(ptr1, ptr2, memo):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            
            if text1[ptr1] == text2[ptr2]:
                return 1 + helper(ptr1+1, ptr2+1, memo)
            
            if (ptr1, ptr2) in memo:
                return memo[(ptr1, ptr2)]
            else:
                memo[(ptr1, ptr2)] = max(helper(ptr1+1, ptr2, memo), helper(ptr1, ptr2+1, memo))
            return memo[(ptr1, ptr2)]

        return helper(0, 0, memo)


class Solution5:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1), len(text2)
        dp = [[""]*(m+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + text1[i]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=len)
        
        print("LCS:",dp[-1][-1])
        return len(dp[-1][-1])

# Unit Test
import unittest
class longestConsecutiveCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_longestConsecutive(self):

        for Sol in [Solution1(), Solution2(), Solution3(), Solution4(), Solution5()]:
            func = Sol.longestCommonSubsequence

            self.assertEqual(func("acde", "ace"), 3)
            self.assertEqual(func("abc", "abc"), 3)
            self.assertEqual(func("abc", "def"), 0)
            self.assertEqual(func("bsbininm", "jmjkbkjkv"), 1)
            self.assertEqual(func("oxcpqrsvwf", "shmtulqrypy"), 2)








if __name__ == '__main__':
    unittest.main()


