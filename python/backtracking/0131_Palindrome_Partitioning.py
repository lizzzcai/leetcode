'''
15/07/2020

131. Palindrome Partitioning - Medium

Tag: Backtracking

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

'''

from typing import List
# Solution
class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        '''
        time: O(n!)
        Space: O(n*len(s))
        '''
        res = []
        if not s:
            return res
        
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def backtrack(s: str, path: List[str], res: List[List[str]]):
            if not s:
                res.append(path[:])
                return
            
            for i in range(1, len(s)+1):
                if is_palindrome(s[:i]):
                    backtrack(s[i:], path+[s[:i]], res)
        
        
        backtrack(s, [], res)
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
            func = Sol.partition
            self.assertEqual(func("aab"), [["a","a","b"],["aa","b"]])
            self.assertEqual(func("aaa"), [["a","a","a"],["a","aa"],["aa","a"],["aaa"]])


if __name__ == '__main__':
    unittest.main()