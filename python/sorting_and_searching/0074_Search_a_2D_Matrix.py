'''
03/05/2020

74. Search a 2D Matrix - Easy

Tag: Binary Search

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(log(m+n))
    Space complexity : O(1)
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        l, r = 0, m*n-1
        while l <= r:
            mid = (l+r) // 2
            i,j = mid // n, mid % n
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.searchMatrix
            self.assertEqual(func([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3), True)
            self.assertEqual(func([], 3), False)
            self.assertEqual(func([[1,3,5,7]], 3), True)



if __name__ == '__main__':
    unittest.main()