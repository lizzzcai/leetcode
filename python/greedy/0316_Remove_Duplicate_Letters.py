'''
17/05/2020

316. Remove Duplicate Letters - Hard

Tag: Stack, Greedy

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

'''

from typing import List
import collections
# Solution
class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        https://leetcode.com/problems/remove-duplicate-letters/discuss/76769/Java-solution-using-Stack-with-comments
        Time:O(N)
        Space:O(N)
        '''
        count = collections.Counter(s)
        stack = []
        visited = set()
        
        for ch in s:
            count[ch] -= 1
            if ch in visited:
                continue
            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
        
        return ''.join(stack)
            
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.removeDuplicateLetters
            self.assertEqual(func('bcabc'), 'abc')
            self.assertEqual(func('cbacdcbc'), 'acdb')


if __name__ == '__main__':
    unittest.main()