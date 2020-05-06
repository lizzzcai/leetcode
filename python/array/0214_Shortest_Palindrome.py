'''
06/05/2020

214. Shortest Palindrome - Hard

Tag: String

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"

'''

from typing import List
# Solution
class Solution1:
    def shortestPalindrome(self, s: str) -> str:
        '''
        Brute force
        Time: O(n^2)
        Space: O(n)
        find the largest palindrome segment from the beginning of the string,
        append the reverse of the rest to the begining of the string
        
        '''
        n = len(s)
        rev = s[::-1]
        j = 0
        for i in range(n):
            if s[:n-i] == rev[i:]:
                return rev[:i]+s
        
        return ""

class Solution2:
    def shortestPalindrome(self, s: str) -> str:
        '''
        Time: O(n^2)
        Space: O(n)
        Two pointers and recursion 
        '''
        n = len(s)
        i = 0
        for j in range(n-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        
        if i == n:
            return s
        
        remain_rev = s[i:n]
        remain_rev = remain_rev[::-1]
        return remain_rev + self.shortestPalindrome(s[:i]) + s[i:]


class Solution3:
    def shortestPalindrome(self, s: str) -> str:
        '''
        Time: O(n)
        Space: O(n)
        KMP
        '''
        
        n = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = 2*n+1
        # create lookup table
        f = [0]*n_new
        for i in range(1, n_new):
            t = f[i-1]
            while t > 0 and s_new[i] != s_new[t]:
                t = f[t-1]
            if s_new[i] == s_new[t]:
                 t += 1
            f[i] = t
        
        return rev[:n-f[n_new-1]] + s


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        rolling hash
        Time: O(n)
        Space: O(1)
        https://leetcode.com/problems/shortest-palindrome/discuss/60153/8-line-O(n)-method-using-Rabin-Karp-rolling-hash
        http://courses.csail.mit.edu/6.006/spring11/rec/rec06.pdf
        '''
        n = len(s)
        if n <= 1:
            return s
        

        MOD = 10 ** 9 + 7
        P = 113
        INV_P = pow(P, MOD-2, MOD)
        
        def code(t):
            return ord(t) - ord('a')+1
        
        hash_s, hash_r = 0, 0
        power = 1
        p = -1
        for i in range(n):
            # ->
            hash_s = (hash_s + code(s[i])*power) % MOD
            # <-
            hash_r = (hash_r*P + code(s[i])) % MOD
            power = power * P % MOD
            if hash_s == hash_r:
                p = i
        
        return s[p+1:][::-1] + s
        


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.shortestPalindrome
            self.assertEqual(func("aacecaaa"), "aaacecaaa")
            self.assertEqual(func("abcd"), "dcbabcd")

if __name__ == '__main__':
    unittest.main()