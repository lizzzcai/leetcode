'''
15/07/2020

151. Reverse Words in a String - Medium

Tag: String

Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def reverseWords(self, s: str) -> str:
        s = [x for x in s.strip(" ").split(" ") if x]
        return ' '.join(s[::-1])

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.reverseWords
            self.assertEqual(func("the sky is blue"), "blue is sky the")
            self.assertEqual(func("  hello world!  "), "world! hello")
            self.assertEqual(func("a good   example"), "example good a")



if __name__ == '__main__':
    unittest.main()