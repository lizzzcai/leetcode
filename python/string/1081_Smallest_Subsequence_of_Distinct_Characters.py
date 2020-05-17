'''
17/05/2020

1081. Smallest Subsequence of Distinct Characters - Medium

Tag: String

Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"

'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(26)
    '''
    def smallestSubsequence(self, text: str) -> str:
        last = {c:i for i,c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        
        return ''.join(stack)

class Solution2:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def smallestSubsequence(self, text: str) -> str:
        count = collections.Counter(text)
        visited, stack = set(), []
        
        for ch in text:
            count[ch] -= 1
            if ch not in visited:
                # if stack[-1] > ch and stack[-1] will comes in later, we can remove it
                while stack and stack[-1] > ch and count[stack[-1]] > 0:
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
        for Sol in [Solution1(), Solution2()]:
            func = Sol.smallestSubsequence
            self.assertEqual(func("cdadabcc"), "adbc")
            self.assertEqual(func("abcd"), "abcd")
            self.assertEqual(func("ecbacba"), "eacb")
            self.assertEqual(func("leetcode"), "letcod")


if __name__ == '__main__':
    unittest.main()