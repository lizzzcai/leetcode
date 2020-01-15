'''
15/01/2020

14. Longest Common Prefix - Easy

Tag: String

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''

from typing import List
# Solution
class Solution:
    '''
    Time complexity : O(n*m)
    Space complexity : O(1)
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        
        for idx, ch in enumerate(strs[0]):
            for other in strs:
                if idx >= len(other) or other[idx] != ch:
                    return res
            res += ch
        
        return res
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().longestCommonPrefix
        self.assertEqual(func(["flower","flow","flight"]), "fl")
        self.assertEqual(func(["dog","racecar","car"]), "")
        self.assertEqual(func([]), "")



if __name__ == '__main__':
    unittest.main()