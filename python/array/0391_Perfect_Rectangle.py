'''
06/01/2020

1. Two Sum - Easy

Tag: Array, Set, Hash Table

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
 
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        '''
        1. sum of area == area
        2. perfect rectangle should appear only one time,
            interpoints should appear only 2, 4 time. (T-junction or cross)
        
        only sum of area is not enough, case:  [[0,0,1,1],[0,1,3,2],[1,0,2,2]]
        '''

        corner=set()
        min_x,min_y,max_x,max_y,area=float('inf'),float('inf'),float('-inf'),float('-inf'),0
        for x1,y1,x2,y2 in rectangles:
            if x1<=min_x and y1<=min_y: min_x,min_y=x1,y1
            if x2>=max_x and y2>=max_y: max_x,max_y=x2,y2
            area+=(x2-x1)*(y2-y1)
            corner^={(x1,y1),(x2,y2),(x1,y2),(x2,y1)}

        return corner=={(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)} and area==(max_x-min_x) * (max_y-min_y)



class Solution2:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        '''
        1. sum of area == area
        2. perfect rectangle should appear only one time,
            interpoints should appear only 2, 4 time. (T-junction or cross)
        
        only sum of area is not enough, case:  [[0,0,1,1],[0,1,3,2],[1,0,2,2]]
        '''

        # record the max/min boundary of perfect rectangle
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')
        count = {}
        area_sum = 0
        # [x1, y1, x2, y2]
        for x1, y1, x2, y2 in rectangles:
            # get the max/min boundary of perfect rectangle
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            # add four count into count dict
            count[(x1, y1)] = count.get((x1, y1), 0) + 1 # x1, y1
            count[(x1, y2)] = count.get((x1, y2), 0) + 1 # x1, y2
            count[(x2, y1)] = count.get((x2, y1), 0) + 1 # x2, y1
            count[(x2, y2)] = count.get((x2, y2), 0) + 1 # x2, y2
            
            area_sum += (x2 - x1)*(y2 - y1)
        
        # check the area sum
        if area_sum != (max_x-min_x) * (max_y-min_y):
            return False
        
        # set of 4 points of perfect rectangle.
        outter_points_set = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        
        # check if the 4 outter points in the count
        for point in outter_points_set:
            if point not in count or count[point] != 1:
                return False
        
        # check if inner points fit rule 2
        for key, val in count.items():
            if key not in outter_points_set and not (val == 2 or val == 4):
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

        for func in [Solution1().isRectangleCover, Solution2().isRectangleCover]:
            rectangles = [
            [1,1,3,3],
            [3,1,4,2],
            [3,2,4,4],
            [1,3,2,4],
            [2,3,3,4]
            ]        
            self.assertEqual(func(rectangles), True)
            rectangles = [
            [1,1,2,3],
            [1,3,2,4],
            [3,1,4,2],
            [3,2,4,4]
            ]
            self.assertEqual(func(rectangles), False)

            rectangles = [
            [1,1,3,3],
            [3,1,4,2],
            [1,3,2,4],
            [3,2,4,4]
            ]

            self.assertEqual(func(rectangles), False)

            rectangles = [
            [1,1,3,3],
            [3,1,4,2],
            [1,3,2,4],
            [2,2,4,4]
            ]
            self.assertEqual(func(rectangles), False)




if __name__ == '__main__':
    unittest.main()