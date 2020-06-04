'''
04/06/2020

344. Reverse String - Easy

Tag: Two Pointers, String

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

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j]= s[j], s[i]
            i += 1
            j -= 1
        return s

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.reverseString
            self.assertEqual(func(["h","e","l","l","o"]), ["o","l","l","e","h"])
            self.assertEqual(func(["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])


if __name__ == '__main__':
    unittest.main()