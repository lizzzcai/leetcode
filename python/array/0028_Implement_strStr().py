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
class Solution1:
    '''
    Time complexity : O(n), O(mn) if comapre char by char
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

# Solution rabin Karp
'''
Time: O(n)
Space:O(1)
'''
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle is empty
        if not needle:
            return 0
        
        # check the first case
        n = len(needle)
        if haystack[:n] == needle:
            return 0
        
        # get the hash of sliding windows
        hash_needle = sum(ord(x) for x in needle)       
        hash_window = sum(ord(x) for x in haystack[:n])

        # iterate and check the haystack[i+1, i+1+n]
        for i in range(0, len(haystack)-n):
            hash_window -= ord(haystack[i])
            hash_window += ord(haystack[i+n])
            if hash_window == hash_needle:
                if haystack[i+1:i+n+1] == needle:
                    return i+1
                
        return -1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution2().strStr
        self.assertEqual(func("hello", "ll"), 2)
        self.assertEqual(func("aaaaa", "bba"), -1)
        self.assertEqual(func("aaaaa", ""), 0)
        


if __name__ == '__main__':
    unittest.main()