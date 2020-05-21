'''
19/05/2020

1446. Consecutive Characters - Easy

Tag: String

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def maxPower(self, s: str) -> int:
        res = 0
        i = 0
        
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j-i > res:
                res = j-i
            
            i = j
        
        return res

import itertools
class Solution2:
    def maxPower(self, s: str) -> int:
        
        return max(len(list(b)) for a, b in itertools.groupby(s))

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.maxPower
            self.assertEqual(func("leetcode"), 2)
            self.assertEqual(func("abbcccddddeeeeedcba"), 5)
            self.assertEqual(func("triplepillooooow"), 5)
            self.assertEqual(func("hooraaaaaaaaaaay"), 11)
            self.assertEqual(func("tourist"), 1)



if __name__ == '__main__':
    unittest.main()