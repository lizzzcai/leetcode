'''
23/06/2020

42. Trapping Rain Water - Hard

Tag: Array, Two Pointers, Stack

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def trap(self, height: List[int]) -> int:
        ans = 0
        left_max, right_max = 0, 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max-height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max-height[right]
                right -= 1
        
        return ans

class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        curr = 0
        stack = []
        while curr < len(height):
            while stack and height[curr] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = curr - stack[-1] - 1
                bounded_height = min(height[curr], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(curr)
            curr += 1
        return ans
                
                

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.trap
            self.assertEqual(func([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

if __name__ == '__main__':
    unittest.main()