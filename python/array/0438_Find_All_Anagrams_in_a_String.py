'''
14/01/2020

438. Find All Anagrams in a String - Medium

Tag: Array, Hash Table, Sliding Window

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
# Solution
class Solution:
    '''
    Sliding Window
    https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
    
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hmap = {}
        for ch in p:
            hmap[ch] = hmap.setdefault(ch, 0) + 1
        count = len(hmap)
        
        length = len(p)
        res = []        
        left = 0
        
        for i in range(len(s)):
    
            if s[i] in hmap:
                hmap[s[i]] = hmap[s[i]] - 1
                if hmap[s[i]] == 0:
                    count -= 1
                    
            while count == 0:
                if s[left] in hmap:
                    hmap[s[left]] = hmap[s[left]] + 1
                    if hmap[s[left]] > 0:
                        count += 1
                
                if i - left + 1 == length:
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
        func = Solution().findAnagrams
        self.assertEqual(func("abab", "ab"), [0, 1, 2])
        self.assertEqual(func("cbaebabacd", "abc"), [0, 6])

if __name__ == '__main__':
    unittest.main()