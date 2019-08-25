"""
25/08/2019
56. Merge Intervals - Medium
Tag: Greedy

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.



"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        
        # sort the list by the end time
        intervals.sort(key=lambda x:x[0])
        intervals = iter(intervals)
        # init the result list and put the first schedule to it
        res = [next(intervals)]
        
        for intv in intervals:
            # get the latest schedule from the result list
            prev = res[-1]
            # compare if overlap
            if intv[0] <= prev[1]: # if overlap, modify the end time to merge them
                res[-1][1] = max(prev[1], intv[1])
            else:
                res.append(intv)
                
        return res



# Unit Test
import unittest
class addTwoNumbersCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_merge(self):
        func = Solution().merge
        # test 1
        self.assertEqual(func([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])

        # test 2
        self.assertEqual(func([[1,4],[4,5]]), [[1,5]])

        # test 3
        self.assertEqual(func([[1,4],[0,4]]), [[0,4]])

        # test 4
        self.assertEqual(func([]), [])




if __name__ == '__main__':
    unittest.main()