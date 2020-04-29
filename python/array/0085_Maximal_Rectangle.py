'''
30/04/2020

85. Maximal Rectangle - Hard

Tag: Array, Stack, Hash Table, Dynamic Programming

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

'''

from typing import List
# Solution

class Solution1:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution

        Time: O(m*(3n))
        Space: O(n)

        '''
        
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        heights = [0]*n
        left = [-1]*n
        right = [n]*n
        max_area = 0
        for r in range(len(matrix)):
            curr_left = -1
            curr_right = n
            for c in range(n):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
                
                # calculate the left boundary
                if matrix[r][c] == "1":
                    left[c] = max(curr_left, left[c])
                else:
                    left[c] = -1
                    curr_left = c
            
            # calculate right boundary
            for c in range(n-1,-1,-1):
                if matrix[r][c] == "1":
                    right[c] = min(curr_right, right[c])
                else:
                    right[c] = n
                    curr_right = c
            
            for c in range(n):
                if heights[c]:
                    max_area = max(max_area, heights[c]*(right[c]-left[c]-1))

        
        return max_area


class Solution2:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        with refer 84
        '''

        
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        heights = [0]*n
        max_area = 0
        for r in range(len(matrix)):
            stack = []
            for c in range(n):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

                while stack and heights[c] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    if stack:
                        w = c - stack[-1] - 1
                    else:
                        w = c
                    max_area = max(max_area, h*w)
                stack.append(c)
            
            while stack:
                h = heights[stack.pop()]
                if stack:
                    w = n - stack[-1] - 1
                else:
                    w = n
                max_area = max(max_area, h*w)
                    
        
        return max_area

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.maximalRectangle
            self.assertEqual(func([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 6)
            self.assertEqual(func([["1","0","1","0","0"],["1","1","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 10)
            self.assertEqual(func([["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]), 9)
if __name__ == '__main__':
    unittest.main()