'''
15/04/2020

796. Rotate String - Easy

Tag: String

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.

'''

from typing import List
# Solution
class Solution1:
    '''
    Brute Force
    O(N^2)
    O(1)
    '''
    def rotateString(self, A: str, B: str) -> bool:
        n = len(A)
        m = len(B)

        if n != m:
            return False
        
        if n == 0:
            return True
        
        for s in range(n):
            if all(A[(s+i) % n] == B[i] for i in range(n)):
                return True
        
        return False

class Solution2:
    def rotateString(self, A: str, B: str) -> bool:
        '''
        Simple Check
        All rotations of A are contained in A+A. Thus, we can simply check whether B is a substring of A+A. We also need to check A.length == B.length
        '''
        return len(A) == len(B) and B in A+A


class Solution3:
    def rotateString(self, A: str, B: str) -> bool:
        '''
        Rolling hash
        
        
        O(n)
        O(n)
        '''
        
        MOD = 10 ** 9 + 7
        P = 113
        Pinv = pow(P, MOD-2, MOD) # pow(x, y, z) is equal to x^y % z
        
        hb = 0
        power = 1
        for x in B:
            code = ord(x) - ord('a') + 1
            hb = (hb + power*code) % MOD
            power = power * P % MOD
        
        ha = 0
        power = 1
        for x in A:
            code = ord(x) - ord('a') + 1
            ha = (ha + power*code) % MOD
            power = power * P % MOD
        
        if ha == hb and A == B:
            return True
        
        for i, x in enumerate(A):
            code = ord(x) - ord('a') + 1
            ha += power * code
            ha -= code
            ha *= Pinv
            ha %= MOD
            if ha == hb and A[i+1:] + A[:i+1] == B:
                return True
            

class Solution4:
    def rotateString(self, A: str, B: str) -> bool:
        '''
        KMP(Knuth-Morris-Pratt) 
        
        https://leetcode.com/articles/rotate-string/
        
        O(N) where N is the length of A
        O(N) to create shift table shifts
        '''

        N = len(A)
        if N != len(B):
            return False
        if N == 0:
            return True
        
        # Compute shift table
        shifts = [1] * (N+1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right+1] = right - left
            left += 1
        
        # Find match of B in A+A
        match_len = 0
        for char in A+A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]
                
            match_len += 1
            if match_len == N:
                return True
        
        return False

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3(), Solution4()]:
            func = Sol.rotateString
            self.assertEqual(func('abcde', 'cdeab'), True)
            self.assertEqual(func('abcde', 'abced'), False)
            self.assertEqual(func("clrwmpkwru", "wmpkwruclr"), True)


if __name__ == '__main__':
    unittest.main()