'''
09/06/2020

792. Number of Matching Subsequences - Medium

Tag: Array 

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].

'''

from typing import List
import collections
# Solution
class Solution1:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        '''
        https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
        Time: O(len(S)+sum(len(w)))
        '''
        ans = 0
        nxt = collections.defaultdict(list)
        nxt['#'] = words
        for ch in '#'+S:
            prev = nxt[ch]
            del nxt[ch]
            
            for w in prev:
                if len(w) == 0:
                    ans += 1
                else:
                    c = w[0]
                    nxt[c].append(w[1:])
        
        return ans

import bisect
class Solution2:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        '''
        https://leetcode.com/problems/is-subsequence/discuss/679493/python-two-pointers-and-NlogN-follow-up-by-binary-search
        Time: O(len(S)+sum(len(w))logn)
        '''
        indexs = collections.defaultdict(list)
        for idx, x in enumerate(S):
            indexs[x].append(idx)
        
        count = 0
        for w in words:
            prev = 0
            is_subseq = True
            for x in w:
                i = bisect.bisect_left(indexs[x], prev)
                if i == len(indexs[x]):
                    is_subseq = False
                    break
                prev = indexs[x][i]+1
            if is_subseq:
                count += 1

        return count

        


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()， Solution2()]:
            func = Sol.numMatchingSubseq
            self.assertEqual(func("abcde", ["a", "bb", "acd", "ace"]), 3)

if __name__ == '__main__':
    unittest.main()