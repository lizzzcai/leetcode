'''
06/02/2019

48. Rotate Image - Medium

Tag: Array

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

# Solution
class Solution:
    '''
    Time complexity : O(n^2)
    Space complexity : O(1)
    '''
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix[0])
        tmp = [0] * 4
        print(f"row range: {n // 2 + n % 2}, col range: {n // 2}")
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                #tmp = [0] * 4
                row, col = i, j
                print(f"row: {row}, col: {col}")
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # rotate 4 elements
                for k in range(4):
                    print(f"rotate ({row}, {col}) with {(k - 1) % 4}")
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row
        return matrix
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().rotate
        self.assertEqual(func([
                            [1,2,3],
                            [4,5,6],
                            [7,8,9]
                            ]), [
                                [7,4,1],
                                [8,5,2],
                                [9,6,3]
                                ]
                                )
        self.assertEqual(func([
                            [ 5, 1, 9,11],
                            [ 2, 4, 8,10],
                            [13, 3, 6, 7],
                            [15,14,12,16]
                            ]), [
                                [15,13, 2, 5],
                                [14, 3, 4, 1],
                                [12, 6, 8, 9],
                                [16, 7,10,11]
                                ])

if __name__ == '__main__':
    unittest.main()