'''
14/01/2020

567. Permutation in String - Medium

Tag: Two Pointers, Sliding Window, Array

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

'''

from typing import List
# Solution
class Solution1:
    '''
    Two Pointers, from 438. Find All Anagrams in a String
    Time complexity : O(2l1+l2)
    Space complexity : O(l1)
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        two pointers
        '''
        if len(s1) > len(s2):
            return False
        
        # create hash table for s1
        hmap = {}
        for ch in s1:
            hmap[ch] = hmap.setdefault(ch, 0) + 1
            
        # count the unique char in s1
        count = len(hmap)
        
        # length of s1
        length = len(s1)
        
        # left pointer
        left = 0
        
        # right pointer start
        for i in range(len(s2)):
            if s2[i] in hmap:
                hmap[s2[i]] -= 1
                if hmap[s2[i]] == 0:
                    count -= 1
                    
            while count == 0:
                # check if the length of right - left match length, (left, right]
                if i - left + 1 == length:
                    return True
                
                if s2[left] in hmap:
                    hmap[s2[left]] += 1
                    if hmap[s2[left]] > 0:
                        count += 1
                
                left += 1
                
        return False
            

class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        sliding window
        Time: O(l1+26*(l2-l1))
        Space: O(1)
        '''
        if len(s1) > len(s2):
            return False
        
        s1map = [0] * 26
        s2map = [0] * 26
        
        for i in range(len(s1)):
            s1map[ord(s1[i])-ord('a')] += 1
            s2map[ord(s2[i])-ord('a')] += 1
        
        for i in range(len(s2)-len(s1)):
            if self.match(s1map, s2map):
                return True
            s2map[ord(s2[i+len(s1)])-ord('a')] += 1
            s2map[ord(s2[i])-ord('a')] -= 1
        
        return self.match(s1map, s2map)
            
    def match(self, s1map, s2map):
        for i in range(26):
            if s1map[i] != s2map[i]:
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
        func = Solution1().checkInclusion
        self.assertEqual(func("ab", "eidboaoo"), False)
        self.assertEqual(func("ab", "eidbaoo"), True)
        self.assertEqual(func("eidbaoo", "ab"), False)

        func = Solution2().checkInclusion
        self.assertEqual(func("ab", "eidboaoo"), False)
        self.assertEqual(func("ab", "eidbaoo"), True)
        self.assertEqual(func("eidbaoo", "ab"), False)

if __name__ == '__main__':
    unittest.main()