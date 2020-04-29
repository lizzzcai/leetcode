'''
09/02/2020

84. Largest Rectangle in Histogram - Hard

Tag: Array, Stack

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10


'''

from typing import List
# Solution

class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        max_area = 0
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                max_area = max(max_area, h*w)
            stack.append(i)
        
        while stack:
            h = heights[stack.pop()]
            if stack:
                w = n - stack[-1] - 1
            else:
                w = n
            max_area = max(max_area, h*w)
        
        return max_area

class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        '''
        https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
        '''
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h*w)
            stack.append(i)
        return res



class Solution3:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)
        Time: O(n)
        Space:O(n)
        
        '''
        if not heights:
            return 0
        n = len(heights)
        # create two arries to store the idx of historgram which
        # less than the current i.
        less_from_left = [0] * n
        less_from_right = [0] * n
        less_from_left[0] = -1
        less_from_right[n-1] = n
        
        # iterate from left to right to fill less_from_left
        for i in range(1,n):
            p = i-1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_from_left[p]
            less_from_left[i] = p
        
        # iterate from right to left to fill less_from_right
        for i in range(n-2, -1, -1):
            p = i+1
            while p < n and heights[p] >= heights[i]:
                p = less_from_right[p]
            less_from_right[i] = p
            
        # get the max rectangle area by iterate the heights
        max_rect_area = 0
        for i in range(n):
            max_rect_area = max(max_rect_area, heights[i]*(less_from_right[i]-less_from_left[i]-1))
        
        return max_rect_area

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):

        for Sol in [Solution1(),Solution2(),Solution3()]:
            func = Sol.largestRectangleArea
            self.assertEqual(func([2,1,5,6,2,3]), 10)

if __name__ == '__main__':
    unittest.main()