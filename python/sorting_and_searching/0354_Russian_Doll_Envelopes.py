'''
08/06/2020

354. Russian Doll Envelopes - Hard

Tag: Binary Search, Dynamic Programming

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

'''

from typing import List
# Solution
class Solution1:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        https://leetcode.com/problems/russian-doll-envelopes/discuss/82763/Java-NLogN-Solution-with-Explanation
        Time: O(nlogn)
        Space: O(n)
        '''
        n = len(envelopes)
        if n <= 1:
            return n
        
        # asend with width and desend with height
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        # find the longest increasing subsequence
        size = 0
        tails = [0]*n
        
        for _, h in envelopes:
            l, r = 0, size-1
            while l <= r:
                mid = (l+r) // 2
                if tails[mid] >= h:
                    r = mid - 1
                else:
                    l = mid + 1
            
            tails[l] = h
            size = max(size, l+1)
        
        return size

import bisect
class Solution2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        Time: O(nlogn)
        Space: O(n)
        '''
        n = len(envelopes)
        if n <= 1:
            return n
        
        # asend with width and desend with height
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        # find the longest increasing subsequence
        size = 0
        tails = [0]*n
        
        for _, h in envelopes:
            l = bisect.bisect_left(tails[:size],h)
            tails[l] = h
            size = max(size, l+1)
        
        return size
                                  

class Solution3:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        using bisect
        Time: O(nlogn)
        Space: O(n)
        '''
        n = len(envelopes)
        if n <= 1:
            return n
        
        # asend with width and desend with height
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        # find the longest increasing subsequence
        size = 0
        tails = []
        for _, h in envelopes:
            l = bisect.bisect_left(tails,h)
            if l < len(tails):
                tails[l] = h
            else:
                tails.append(h)
                size = max(size, l+1)
        
        return size


class Solution4:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        sort+dp
        TLE
        Time: O(n^2)
        Space: O(n)
        '''
        n = len(envelopes)
        if n <= 1:
            return n
        
        # asend with width and desend with height
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        # find the longest increasing subsequence

        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
                    

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3(), Solution4()]:
            func = Sol.maxEnvelopes
            self.assertEqual(func([[5,4],[6,4],[6,7],[2,3]]), 3)

if __name__ == '__main__':
    unittest.main()