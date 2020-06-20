'''
20/06/2020

275. H-Index II - Medium

Tag: Binary Search

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?

'''

from typing import List
# Solution
class Solution1:
    '''

    The basic idea of this solution is to use binary search to find the minimum index such that

    citations[index] >= length(citations) - index

    Time complexity : O(logn)
    Space complexity : O(1)
    '''
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        N = len(citations)
        l, r = 0, N-1
        
        while l <= r:
            mid = (l+r)//2
            # num of paper = N-mid-1, h: citations[mid]
            h = N-mid
            if h == citations[mid]:
                return h
            elif h > citations[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return N-l

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.hIndex
            self.assertEqual(func([]), 0)
            self.assertEqual(func([0,1,3,5,6]), 3)

if __name__ == '__main__':
    unittest.main()