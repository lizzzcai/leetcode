'''
17/05/2020

438. Find All Anagrams in a String - Medium

Tag: Hash Table

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from typing import List
import collections
# Solution
class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        O(S)
        O(P)
        '''
        count = {}
        for x in p:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        remain = len(count)
        length = len(p)
        left = 0
        res = []
        
        for right, ch in enumerate(s):
            if ch in count:
                count[ch] -= 1
                if count[ch] == 0:
                    remain -= 1
            
            while remain == 0:
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] > 0:
                        remain += 1
                
                if right - left + 1 == length:
                    res.append(left)
                
                left += 1
                    
                
        
        return res
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findAnagrams
            self.assertEqual(func('cbaebabacd', 'abc'), [0,6])
            self.assertEqual(func('abab', 'ab'), [0,1,2])


if __name__ == '__main__':
    unittest.main()