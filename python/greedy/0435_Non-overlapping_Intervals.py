"""
25/08/2019
435. Non-overlapping Intervals - Medium
Tag: Greedy

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.


"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        # sort the array by the end value by asend
        intervals.sort(key = lambda x:x[1], reverse = False)
        # convert to generator
        intervals = iter(intervals)
        # get the first end time and init the count
        curr_end, cnt = next(intervals)[1], 0
        # list to store the intervals to erase
        erase_indexs = []
        
        for idx, intv in enumerate(intervals):
            if intv[0] >= curr_end: # no overlap if start >= end
                # udate the current end
                curr_end = intv[1]
            else:
                erase_indexs.append(idx)
                cnt += 1
                #curr_end = min(curr_end, intv[1]) # because we sort the array, so larger one is the overlap one, we erase it.
        
        return cnt



# Unit Test
import unittest
class addTwoNumbersCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_eraseOverlapIntervals(self):
        func = Solution().eraseOverlapIntervals
        # test 1
        self.assertEqual(func([[1,2],[2,3],[3,4],[1,3]]), 1)

        # test 2
        self.assertEqual(func([[1,2],[1,2],[1,2]]), 2)

        # test 3
        self.assertEqual(func([[1,2],[2,3]]), 0)





if __name__ == '__main__':
    unittest.main()