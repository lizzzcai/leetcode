'''
05/04/2020
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
class Solution1:
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
                if idx == len(other) or other[idx] != ch:
                    return res
            res += ch
        
        return res

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        '''
        Time: O(S)
        Space: O(1)
        
        '''
        if not strs:
            return ''
        
        prefix = strs[0]
        for i in range(len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
            if not prefix:
                return ''
        
        return prefix


class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        '''
        divide and conquer
        Time: O(S), S = m*n
        Space: O(mlogn)
        
        '''
        
        def divide(l, r):
            if l >= r:
                return strs[l]

            mid = (l+r) // 2

            left = divide(l, mid)
            right = divide(mid+1, r)

            return conquer(left, right)
        
        def conquer(str1, str2):
            min_len = min(len(str1), len(str2))
            
            for i in range(min_len):
                if str1[i] != str2[i]:
                    return str1[:i]
            
            return str1[:min_len]
        
        if not strs:
            return ''
        
        return divide(0, len(strs)-1)
    
        
            

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):

        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.longestCommonPrefix
            self.assertEqual(func(["flower","flow","flight"]), "fl")
            self.assertEqual(func(["dog","racecar","car"]), "")
            self.assertEqual(func([]), "")



if __name__ == '__main__':
    unittest.main()