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

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.rotateString
            self.assertEqual(func('abcde', 'cdeab'), True)
            self.assertEqual(func('abcde', 'abced'), False)
            self.assertEqual(func("clrwmpkwru", "wmpkwruclr"), True)


if __name__ == '__main__':
    unittest.main()