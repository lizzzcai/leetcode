'''
07/04/2020

49. Group Anagrams - Medium

Tag: Hash Table, String

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''

from typing import List
import collections
# Solution
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Time: O(NKlogK), N is the length of strs, K is the max length of string in strs. O(N)
               as we iterate each string.
               
        Space: O(NK)
        '''
        hmap = collections.defaultdict(list)
        for s in strs:
            hmap[tuple(sorted(s))].append(s)
        
        return list(hmap.values())

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.groupAnagrams
            self.assertEqual(func(["eat","tea","tan","ate","nat","bat"]), [["eat","tea","ate"],["tan","nat"],["bat"]])

if __name__ == '__main__':
    unittest.main()