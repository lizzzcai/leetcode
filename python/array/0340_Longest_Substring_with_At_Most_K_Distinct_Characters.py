'''
31/03/2020

340. Longest Substring with At Most K Distinct Characters - Hard

Tag: Hash Table

Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Example
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def lengthOfLongestSubstringKDistinct(self, s, k):
        hmap = {}

        n = len(s)
        left = 0
        count = 0
        res = 0
        for right in range(n):
            if s[right] not in hmap:
                hmap[s[right]] = 0
            
            if hmap[s[right]] == 0:
                count += 1
            
            hmap[s[right]] += 1
             
            
            while count > k:
                hmap[s[left]] -= 1
                if hmap[s[left]] == 0:
                    count -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
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
            func = Sol.lengthOfLongestSubstringKDistinct
            self.assertEqual(func("eceba", 3), 4)
            self.assertEqual(func("WORLD", 4), 4)


if __name__ == '__main__':
    unittest.main()