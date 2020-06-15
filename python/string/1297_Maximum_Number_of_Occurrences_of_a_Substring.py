'''
13/06/2020

1297. Maximum Number of Occurrences of a Substring - Medium

Tag: String, Bit Manipulation

Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
 

Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
Example 3:

Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3
Example 4:

Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0
 

Constraints:

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.

'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        '''
        https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/discuss/462213/Python-2-lines-Counter
        If a string have ocurrences x times,
        any if its substring must appear at least x times.

        There must be a substring of length minSize, that has the most ocurrences.
        So that we just need to count the ocurrences of all subtring with length minSize.
        '''
        count = collections.defaultdict(int)
        for k in range(len(s)-minSize+1):
            word = s[k:k+minSize]
            count[word] += 1
        
        res = 0
        for w in count:
            if len(set(w)) <= maxLetters:
                res = max(res, count[w])
                
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
            func = Sol.maxFreq
            self.assertEqual(func("aaaa", 1, 3, 3), 2)
            self.assertEqual(func("aababcaab", 2, 3, 4), 2)


if __name__ == '__main__':
    unittest.main()