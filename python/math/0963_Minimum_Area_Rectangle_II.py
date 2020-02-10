'''
10/02/2020

963. Minimum Area Rectangle II - Medium

Tag: Math, Geometry

Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:



Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:



Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:



Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:



Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
 

Note:

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
Answers within 10^-5 of the actual value will be accepted as correct.
'''
import itertools
import collections
from typing import List
# Solution
class Solution1:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        '''
        https://leetcode.com/problems/minimum-area-rectangle-ii/discuss/208377/Python-easy-to-understand-dot-product-O(N3)-AC
        Time: O(N^3)
        Space: O(N)
        
        '''
        min_area = float('inf')
        n = len(points)
        points_set = {(x,y) for x, y in points}
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    # check if v31, v21 are perpendicular
                    # if they are, v31*v21 = 0
                    # (x3-x1)*(x2-x1) + (y3-y1)*(y2-y1) = 0
                    if (x3-x1)*(x2-x1) + (y3-y1)*(y2-y1) == 0:
                        # calculate the possible point 4
                        # x4 = x3+(x2-x1)
                        # y4 = y3+(y2-y1)
                        x4, y4 = x3+(x2-x1), y3+(y2-y1)
                        # check if the point 4 exists,
                        # if yes, calculate the area
                        if (x4, y4) in points_set:
                            # abs(v31)*abs(v21)
                            new_area = (((x3-x1)**2 + (y3-y1)**2)**0.5) * (((x2-x1)**2 + (y2-y1)**2)**0.5)
                            min_area = min(min_area, new_area)
                            
        if min_area == float('inf'):
            return 0
        return min_area

class Solution2:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        '''
        https://leetcode.com/problems/minimum-area-rectangle-ii/discuss/208351/Python-Complex
        Time: O(N^2) average, O(N^3) in worst cases, if all edges can form a rectangle.
        Space: O(N^2)
        '''
        # convert to vector using complex
        # sorted here is to make sure vector have same direction of they are equal.
        # like [1, 1], [-1, -1]
        points = [complex(*z) for z in sorted(points)]
        seen = collections.defaultdict(list) # a dict to store all the edges and its midpoint
        # combination of all the points by 2, and append the midpoint
        for M, N in itertools.combinations(points, 2):
            seen[M-N].append((M+N)/2)
        
        # so for each edge vector, they have same direction and same length, but maybe different starting point
        # we iterate each of them, for each two of midpoint, if the connection of midpoints is perpendicular,
        # then it can form a rectangle, we calculate the area
        min_area = float('inf')
        for edge, midpoints in seen.items():
            for P, Q in itertools.combinations(midpoints, 2):
                # connection of midpoints: v = P-Q
                # if perpendicular, edge * v = 0
                v = P - Q
                if edge.real * v.real == -(edge.imag * v.imag): # edge * v = 0
                    min_area = min(min_area, abs(edge)*abs(v))
        
        if min_area == float('inf'):
            return 0
        return min_area

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().minAreaFreeRect
        self.assertAlmostEqual(func([[1,2],[2,1],[1,0],[0,1]]), 2.)
        self.assertAlmostEqual(func([[0,3],[1,2],[3,1],[1,3],[2,1]]), 0)
        self.assertAlmostEqual(func([[0,1],[2,1],[1,1],[1,0],[2,0]]), 1.)
        self.assertAlmostEqual(func([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]), 2.0)
        self.assertAlmostEqual(func([[0,1],[1,0],[3,2],[2,3],[0,3],[1,1],[3,3],[0,2]]), 3.0)

        func = Solution2().minAreaFreeRect
        self.assertAlmostEqual(func([[1,2],[2,1],[1,0],[0,1]]), 2.)
        self.assertAlmostEqual(func([[0,3],[1,2],[3,1],[1,3],[2,1]]), 0)
        self.assertAlmostEqual(func([[0,1],[2,1],[1,1],[1,0],[2,0]]), 1.)
        self.assertAlmostEqual(func([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]), 2.0)
        self.assertAlmostEqual(func([[0,1],[1,0],[3,2],[2,3],[0,3],[1,1],[3,3],[0,2]]), 3.0)



if __name__ == '__main__':
    unittest.main()

