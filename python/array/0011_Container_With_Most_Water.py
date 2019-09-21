"""
21/09/2019
11. Container With Most Water - Medium
Tag: Array, two pointer


Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height)-1
        while l < r:
            maxArea = max(maxArea, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
                
        

# Unit Test
import unittest
class maxAreaCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_maxArea(self):
        func = Solution().maxArea

        self.assertEqual(func([1,8,6,2,5,4,8,3,7]), 49)






if __name__ == '__main__':
    unittest.main()


