'''
15/08/2020

409. Longest Palindrome - Easy

Tag: Hash Table

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

'''

from typing import List
import collections

class Solution1:
    def longestPalindrome(self, s: str) -> int:
        '''
        Time complexity : O(n)
        Space complexity : O(n)
        '''
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        odd = False
        ans = 0
        for k, v in count.items():
            if v % 2 == 0:
                ans += v
            elif odd == True:
                ans += v-1
            else:
                ans += v
                odd = True
        
        return ans

class Solution2:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        ans = 0
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        
        return ans


class Solution3:
    def longestPalindrome(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        check = set()
        for ch in s:
            if ch in check:
                check.remove(ch)
            else:
                check.add(ch)
        
        if len(check) == 0:
            return len(s)
        
        return len(s) - len(check) + 1


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.longestPalindrome
            self.assertEqual(func("abccccdd"), 7)
            self.assertEqual(func("dd"), 2)
            self.assertEqual(func("d"), 1)
            self.assertEqual(func("abc"), 1)
            self.assertEqual(func(""), 0)





if __name__ == '__main__':
    unittest.main()