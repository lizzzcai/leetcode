'''
07/02/2019

344. Reverse String - Easy

Tag: 

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

# Solution
class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s

class Solution1:
    def reverseString(self, s: 'List[str]') -> 'None':
        return s[::-1]

class Solution2:
        """
        Recursive
        """
    def reverseString(self, s: 'List[str]') -> 'None':
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l // 2:]) + self.reverseString(s[:l // 2])

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().reverseString
        self.assertEqual(func(["h","e","l","l","o"]), ["o","l","l","e","h"])
        self.assertEqual(func(["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])

        func = Solution1().reverseString
        self.assertEqual(func(["h","e","l","l","o"]), ["o","l","l","e","h"])
        self.assertEqual(func(["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])

        func = Solution2().reverseString
        self.assertEqual(func(["h","e","l","l","o"]), ["o","l","l","e","h"])
        self.assertEqual(func(["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])

if __name__ == '__main__':
    unittest.main()