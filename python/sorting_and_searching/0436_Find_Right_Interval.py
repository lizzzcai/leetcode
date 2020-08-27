'''
27/08/2020

436. Find Right Interval - Medium

Tag: Binary Search

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
 

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
 

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        hmap = dict()
        sort = []
        for idx, x in enumerate(intervals):
            hmap[tuple(x)] = idx
            sort.append(tuple(x))
            
        sort = sorted(sort, key=lambda x: x[0])
        res = []
        
        for idx, x in enumerate(intervals):
            i = self.bs(sort, x[1])
            
            if i == n:
                res.append(-1)
            else:
                res.append(hmap[sort[i]])
        return res
            
        
    def bs(self, intervals, target):
        left, right = 0, len(intervals)-1
        while left <= right:
            mid = (left + right) // 2
            tmp = intervals[mid][0]
            if tmp > target:
                right = mid - 1
            elif tmp < target:
                left = mid + 1
            else:
                return mid
        
        return left


class Solution2:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sort = sorted([[x[0], idx] for idx, x in enumerate(intervals)]) + [[float('inf'), -1]]
        res = []
        for x in intervals:
            i = self.bs(sort, x[1])
            res.append(sort[i][1])
        return res
            
        
    def bs(self, intervals, target):
        left, right = 0, len(intervals)-1
        while left <= right:
            mid = (left + right) // 2
            tmp = intervals[mid][0]
            if tmp > target:
                right = mid - 1
            elif tmp < target:
                left = mid + 1
            else:
                return mid
        
        return left
    

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.findRightInterval
            self.assertEqual(func([[1,2]]), [-1])
            self.assertEqual(func([[3,4], [2,3], [1,2]]), [-1,0,1])
            self.assertEqual(func([[1,4], [2,3], [3,4]]), [-1,2,-1])


if __name__ == '__main__':
    unittest.main()