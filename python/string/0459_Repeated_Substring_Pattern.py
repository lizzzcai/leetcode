'''
03/09/2020

459. Repeated Substring Pattern - Easy

Tag: String

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n^2)
    Space complexity : O(n)
    '''
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        i = 0
        count = set()
        
        for i in range(n):
            if s[i] in count:
                count.remove(s[i])
            else:
                count.add(s[i])
            if len(count) == 0:
                size = (i+1)//2
                
                if s[:size]*(n//size) == s:
                    return True
        
        return False
        


class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        If the string S has repeated block, it could be described in terms of pattern.
        S = SpSp (For example, S has two repeatable block at most)
        If we repeat the string, then SS=SpSpSpSp.
        Destroying first and the last pattern by removing each character, we generate a new S2=SxSpSpSy.

        If the string has repeatable pattern inside, S2 should have valid S in its string.
        '''
        ss = s+s
        return s in ss[1:-1]
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.repeatedSubstringPattern
            self.assertEqual(func("abab"), True)
            self.assertEqual(func("aba"), False)
            self.assertEqual(func("abcabcabcabc"), True)
            self.assertEqual(func("ababab"), True)


if __name__ == '__main__':
    unittest.main()