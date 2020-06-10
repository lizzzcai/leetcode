'''
09/06/2020

392. Is Subsequence - Easy

Tag: Binary Search, Dynamic Programming, Greedy

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
Accepted

'''

from typing import List
import collections
import bisect
# Solution

class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
                
        return i == len(s)

class Solution2:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(n)
    '''
    def isSubsequence(self, s: str, t: str) -> bool:
        indexs = collections.defaultdict(list)
        for idx, x in enumerate(t):
            indexs[x].append(idx)
        
        prev = 0
        for x in s:
            i = bisect.bisect_left(indexs[x], prev)
            if i == len(indexs[x]):
                return False
            
            prev = indexs[x][i]+1
        
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
            func = Sol.isSubsequence
            self.assertEqual(func("abc", "ahbgdc"), True)
            self.assertEqual(func("axc", "ahbgdc"), False)


if __name__ == '__main__':
    unittest.main()