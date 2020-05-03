'''
03/05/2020

383. Ransom Note - Easy

Tag: String, Hash Table

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''

import collections
from typing import List
# Solution
class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        O(n+m)
        O(1)
        '''
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0]*26
        
        for s in ransomNote:
            count[ord(s)-ord('a')] += 1
        
        for s in magazine:
            if count[ord(s)-ord('a')] > 0:
                count[ord(s)-ord('a')] -= 1
        
        for x in count:
            if x > 0:
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
        for Sol in [Solution1(), Solution2()]:
            func = Sol.canConstruct
            self.assertEqual(func("a", "b"), False)
            self.assertEqual(func("aa", "ab"), False)
            self.assertEqual(func("aa", "aab"), True)



if __name__ == '__main__':
    unittest.main()