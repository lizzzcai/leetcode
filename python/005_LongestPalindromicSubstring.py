"""
21/12/2018

Tag: Array

5. Longest Palindromic Substring - Medium


Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""

# Expand Around Center
class Solution:
    """
    Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).

    Space complexity : O(1). 
    """    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if len_s < 1:
            return ""
        start, end = 0, 0
        print("str: ", s)
        for i in range(len_s):
            print("len1:")
            # Case 1: the center of a palindrome in each letters. 
            len1 = self.expandAroundCenter(s, i, i)
            print("len2:")
            # Case 2: the center of a palindrome can be in between two letters. 
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            print(f"i: {i}, len1: {len1}, len2: {len2}, length: {length} \n    start: {start}, end: {end}")
            if (length > end - start):
                start = i - (length - 1) // 2
                end = i + length // 2
                print(f"updated! start: {start}, end: {end}")
            print("current res: ", s[start:end+1])
        return s[start:end+1]
        
    def expandAroundCenter(self, s, left, right):
        """
        :type s: str
        :type left: int
        :type right: int
        :rtype: int
        """
        L, R = left, right
        # L = 0 for the beginning case
        while (L >= 0 and R < len(s) and s[L] == s[R]):
            L -= 1
            R += 1
        print("EAC: ", s[L+1:R])
        return R - L - 1    # after while loop terminate, L-1 and R+1 are run. so need to minus

class Solution1:
    """
    Manacher algorithm
    http://en.wikipedia.org/wiki/Longest_palindromic_substring
    Based on this article: http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
    
    Time complexity : O(n).

    Space complexity : O(n). 
    """
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C, R = 0, 0
        for i in range (1, n-1):
            # //P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            i_mirror = 2 * C - i # equal to i' = C - (i -C)
            P[i] = min(R - i, P[i_mirror]) if R > i else 0

            # Attempt to expand palindrome centered at i
            # +1 and -1 to expand one step first.
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((_len, idx) for idx, _len in enumerate(P))
        return s[(centerIndex  - maxLen) // 2: (centerIndex  + maxLen) // 2]

# Unit Test
import unittest
class longestPalindromeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_longestPalindrome(self):
        # SOLUTION 0
        func = Solution().longestPalindrome
        self.assertEqual(func("babad"), "aba")
        self.assertEqual(func("cbbd"), "bb")
        self.assertEqual(func("a"),"a")
        self.assertEqual(func(""),"")

        # SOLUTION 1
        func = Solution1().longestPalindrome
        self.assertEqual(func("babad"), "aba")
        self.assertEqual(func("cbbd"), "bb")
        self.assertEqual(func("a"),"a")
        self.assertEqual(func(""),"")


if __name__ == '__main__':
    unittest.main()
