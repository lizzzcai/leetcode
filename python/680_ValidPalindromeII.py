'''
08/02/2019

680. Valid Palindrome II - Easy

Tag: String, Greedy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

'''

# Solution
class Solution:
    '''
    Greedy

    Intuition

    If the beginning and end characters of a string are the same (ie. s[0] == s[s.length - 1]), 
    then whether the inner characters are a palindrome (s[1], s[2], ..., s[s.length - 2]) uniquely determines whether the entire string is a palindrome.

    Algorithm

    Suppose we want to know whether s[i], s[i+1], ..., s[j] form a palindrome. 
    If i >= j then we are done. If s[i] == s[j] then we may take i++; j--. 
    Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], and we should check both cases.



    Time complexity : O(n)
    Space complexity : O(1) 
    '''
    def validPalindrome(self, s: 'str') -> 'bool':
        def is_pali_range(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
        for i in range(len(s) // 2):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True
                
        
        
class Solution1:
    """
    Brute Force 
    Time complexity : O(n^2)
    Space complexity : O(n) 
    """

    def validPalindrome(self, s: 'str') -> 'bool':
        for i in range(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]:
                return True
        
        return s == s[::-1]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().validPalindrome
        self.assertEqual(func("aba"), True)
        self.assertEqual(func("abca"), True)
        self.assertEqual(func("aabca"), False)





if __name__ == '__main__':
    unittest.main()