'''
07/09/2020

290. Word Pattern - Easy

Tag: Hash Table

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(N)
    Space complexity : O(M)
    '''
    def wordPattern(self, pattern: str, str: str) -> bool:
        mapx = {}
        mapy = {}
        strs = str.split(" ")
        if len(strs) != len(pattern):
            return False
        
        for x, y in zip(pattern, strs):
            if x not in mapx:
                if y in mapy:
                    return False
                else:
                    mapx[x] = y
                    mapy[y] = x
            else:
                if mapx[x] != y:
                    return False
        
        return True
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.wordPattern
            self.assertEqual(func("abba", "dog cat cat dog"), True)
            self.assertEqual(func("abba", "dog cat cat fish"), False)
            self.assertEqual(func("abba", "dog dog dog dog"), False)


if __name__ == '__main__':
    unittest.main()