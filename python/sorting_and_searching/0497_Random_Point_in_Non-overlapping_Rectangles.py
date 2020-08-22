'''
01/08/2020

497. Random Point in Non-overlapping Rectangles - Medium

Tag: Random, Binary Search

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]
Example 2:

Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

'''

from typing import List
import random, bisect
# Solution
class Solution1:
    '''
    Time complexity : O(logn)
    Space complexity : O(n)
    '''
    def __init__(self, rects: List[List[int]]):
        self.rects, self.ranges, sm = rects, [0], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2-x1+1) * (y2-y1+1)
            self.ranges.append(sm)
        
    def pick(self) -> List[int]:
        n = random.randint(0, self.ranges[-1]-1)
        i = bisect.bisect_right(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i-1]
        n -= self.ranges[i-1]
        return [x1 + n % (x2-x1+1), y1 + n // (x2-x1+1)]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1]:
            rects = [[1,1,5,5]]
            obj = Sol(rects)
            param_1 = obj.pick()
            

if __name__ == '__main__':
    unittest.main()