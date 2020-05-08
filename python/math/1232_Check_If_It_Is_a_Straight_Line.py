'''
08/05/2020

1232. Check If It Is a Straight Line - Easy

Tag: Array, Math, Geometry

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        
        is_vertical = False
        slope = 0
        if (coordinates[-1][0]-coordinates[0][0]) == 0:
            is_vertical = True
        else:
            slope = (coordinates[-1][1]-coordinates[0][1]) / (coordinates[-1][0]-coordinates[0][0])
        
        for i in range(1, n-1):
            if is_vertical and coordinates[i][0] !=coordinates[0][0]:
                return False
            if not is_vertical and coordinates[i][0] == coordinates[0][0]:
                return False
            if not is_vertical and (coordinates[i][1]-coordinates[0][1]) / (coordinates[i][0]-coordinates[0][0]) != slope:
                return False
        
        return True


class Solution2:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        # (x2-x1)/(y2-y1) = (x-x1)/(y-y1)
        for x, y in coordinates:
            if (x2-x1)*(y-y1) != (y2-y1)*(x-x1):
                return False
    
        return True

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.checkStraightLine
            self.assertEqual(func([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]), True)
            self.assertEqual(func([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]), False)

if __name__ == '__main__':
    unittest.main()