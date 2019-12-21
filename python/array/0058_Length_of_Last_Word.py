'''
21/12/2019

58. Length of Last Word - Easy

Tag: String

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
 

'''

# Solution
class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def lengthOfLastWord(self, s: str) -> int:
        
        len_of_last_word = 0
        s = s.strip()
        s = s[::-1]

        for char in s:
            if char == ' ':
                break
            len_of_last_word += 1
        return len_of_last_word
        

# Unit Test
import unittest
class lengthOfLastWordCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_lengthOfLastWordCase(self):
        func = Solution().lengthOfLastWord
        self.assertEqual(func(""), 0)
        self.assertEqual(func(" "), 0)
        self.assertEqual(func("world "), 5)
        self.assertEqual(func("  world"), 5)
        self.assertEqual(func("b   a    "), 1)
        self.assertEqual(func("Hello World"), 5)


if __name__ == '__main__':
    unittest.main()