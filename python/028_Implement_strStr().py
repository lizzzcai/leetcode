'''
09/02/2019

28. Implement strStr()- Easy

Tag: String

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

# Solution
class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if needle == "":
            return 0
        l = len(needle)
        for i in range(len(haystack) - l + 1):
            if haystack[i:i+l] == needle:
                return i
        return -1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().strStr
        self.assertEqual(func("hello", "ll"), 2)
        self.assertEqual(func("aaaaa", "bba"), -1)
        self.assertEqual(func("aaaaa", ""), 0)
        


if __name__ == '__main__':
    unittest.main()