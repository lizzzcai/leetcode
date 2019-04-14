'''
08/02/2019

125. Valid Palindrome - Easy

Tag: String

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

# Solution
class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(n) 


    '''
    def isPalindrome(self, s: 'str') -> 'bool':
        print(f"str: {s}")
        s = s.lower()
        clean_s = []
        # chk = [ch.lower() for ch in s if ch.isalnum()]
        for char in s:
            if char >= "a" and char <= "z" or char >= "0" and char <= "9":
                clean_s.append(char)
        print(f"clean str: {clean_s}")
        
        start, end = 0, len(clean_s) - 1
        while start < end:
            if clean_s[start] != clean_s[end]:
                return False
            start += 1
            end -= 1
        return True
                
        
        
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().isPalindrome
        self.assertEqual(func("A man, a plan, a canal: Panama"), True)
        self.assertEqual(func("race a car"), False)
        self.assertEqual(func("0P"), False)





if __name__ == '__main__':
    unittest.main()