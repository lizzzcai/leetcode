'''
10/04/2020

844. Backspace String Compare - Easy

Tag: Two Pointers, Stack

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

'''

from typing import List
import itertools
# Solution
class Solution1:
    def backspaceCompare(self, S: str, T: str) -> bool:
        '''
        Stack
        Time:O(m+n)
        Space:O(m+n)
        '''
        def helper(s):
            stack = []
            for ch in s:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)
        
        return helper(S) == helper(T)


class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            '''
            Time:O(m+n)
            Space:O(1)

            "#a#c"
            from left to right
            if it's a char and skip == 0, then return char
            if its #, then skip += 1
            if skip > 0, we skip one char and skip -= 1
            '''
            skip = 0
            for ch in reversed(s):
                if ch == '#':
                    skip += 1
                else:
                    if skip > 0:
                        skip -= 1
                    else:
                        yield ch
            
        for c1, c2 in itertools.zip_longest(helper(S), helper(T)):
            if c1 != c2:
                return False
        
        return True
            
class Solution3:
    def backspaceCompare(self, S: str, T: str) -> bool:
        '''
        Two pointers
        Time:O(m+n)
        Space:O(1)
        '''
        p1, p2 = len(S)-1, len(T)-1
        skip1, skip2 = 0, 0
        
        while p1 >= 0 or p2 >= 0:
            while p1 >= 0:
                if S[p1] == '#':
                    skip1 += 1
                elif skip1 > 0:
                    skip1 -= 1
                else:
                    break
                p1 -= 1
            
            while p2 >= 0:
                if T[p2] == '#':
                    skip2 += 1
                elif skip2 > 0:
                    skip2 -= 1
                else:
                    break
                p2 -= 1
            
            if (p1 >= 0 and p2 < 0) or (p1 < 0 and p2 >= 0):
                return False
            if p1 >=0 and p2 >= 0 and S[p1] != T[p2]:
                return False
            
            p1 -= 1
            p2 -= 1
        
        return True
            
            
            
        
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.backspaceCompare
            self.assertEqual(func("ab#c", "ad#c"), True)
            self.assertEqual(func("ab##", "c#d#"), True)
            self.assertEqual(func("a##c", "#a#c"), True)
            self.assertEqual(func("a#c", "b"), False)



if __name__ == '__main__':
    unittest.main()