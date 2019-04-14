'''
19/02/2019

240. Search a 2D Matrix II - Medium

Tag: Array, Binary

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

'''

# Solution
class Solution:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        
        n_row, n_col = len(matrix), len(matrix[0])
        
        # check the cols
        left, right = 0, n_col - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[0][mid] > target:
                right = mid - 1
            elif matrix[0][mid] < target:
                left = mid + 1
            else:
                return True
        
        print("left:", left)
        print("right:", right)
        # check which row
        while matrix[-1][right] >= target and right >= 0:
            top, bot = 0, n_row - 1
            while top <= bot:
                mid = (top + bot) // 2
                if matrix[mid][right] > target:
                    bot = mid - 1
                elif matrix[mid][right] < target:
                    top = mid + 1
                else: 
                    return True
            right -= 1
        
        return False
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().searchMatrix
        self.assertEqual(func([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5), True)

if __name__ == '__main__':
    unittest.main()