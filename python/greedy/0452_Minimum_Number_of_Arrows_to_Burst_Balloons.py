"""
25/08/2019
432. Minimum Number of Arrows to Burst Balloons - Medium
Tag: Greedy

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

"""

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        # sort the list by the end time
        points.sort(key=lambda x:x[0])
        points = iter(points)
        # init the result list and put the first schedule to it
        intersect = [next(points)]
        
        for intv in points:
            # get the latest schedule from the result list
            prev = intersect[-1]
            # compare if overlap
            if intv[0] <= prev[1]: # if overlap, modify the end time to merge them
                # update start value
                intersect[-1][0] = max(prev[0], intv[0])
                # update end value
                intersect[-1][1] = min(prev[1], intv[1])
                
            else:
                intersect.append(intv)
        
        print(intersect)
        return len(intersect)


class Solution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0
        
        points.sort(key=lambda x:x[1])
        l, r = points[0][0], points[0][1]
        count = 1
        
        for i in range(1, n):
            left = points[i][0]
            # if overlap
            if left <= r:
                # update the next left boundary if any
                if left > l:
                    l = left
            else:
                # if not overlap, init the l, r boundary and add one shoot
                count += 1
                l, r = points[i][0], points[i][1]
                
                
        return count
                

# Unit Test
import unittest
class addTwoNumbersCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_findMinArrowShots(self):
        func = Solution().findMinArrowShots
        # test 1
        self.assertEqual(func([[10,16], [2,8], [1,6], [7,12]]), 2)

        # test 2
        self.assertEqual(func([]), 0)






if __name__ == '__main__':
    unittest.main()