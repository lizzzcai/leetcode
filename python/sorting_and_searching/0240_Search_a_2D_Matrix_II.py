'''
19/02/2019
18/04/2020

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

class Solution1:
    '''
    Time complexity : O(mn)
    Space complexity : O(1)
    '''
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0]:
            return False
        
        # out of range
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        nRows, nCols = len(matrix), len(matrix[0])
        
        row, col = 0, nCols-1
        
        while row < nRows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False


class Solution2:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        '''
        time: O(nlogn)
        space: O(1)
        
        '''
        
        if not matrix or not matrix[0]:
            return False
        
        # out of range
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        nRows, nCols = len(matrix), len(matrix[0])
        
        # find the rightest col that >= target, so that we can ignore them
        left, right = 0, nCols-1
        while left <= right:
            mid = (left+right) // 2
            if matrix[0][mid] == target:
                return True
            elif matrix[0][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        col = right
        
        # find it from left to right, col by col
        while matrix[-1][col] >= target and col >= 0:
            # find the row that == target
            top, bot = 0, nRows-1
            while top <= bot:
                mid = (top+bot) // 2
                if matrix[mid][col] == target:
                    return True
                elif matrix[mid][col] > target:
                    bot = mid - 1
                else:
                    top  = mid + 1
            col -= 1
        
        return False


class Solution3:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        # out of range
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        def divideAndConquer(matrix, target, startX, startY, endX, endY):
            # mid = start + (end-start) // 2
            midX, midY = startX+(endX-startX)//2, startY+(endY-startY)//2
            # stop if start > end
            if startX > endX or startY > endY:
                return False
            if matrix[midY][midX] == target:
                return True
            elif matrix[midY][midX] > target:
                # mid-1
                zone1 = divideAndConquer(matrix,target,startX,startY,midX-1,midY-1)
                zone2 = divideAndConquer(matrix,target,midX,startY,endX,midY-1)
                zone3 = divideAndConquer(matrix, target, startX,midY,midX-1,endY)
                return zone1 or zone2 or zone3
            else:
                # mid+1
                zone2 = divideAndConquer(matrix,target,midX+1,startY,endX,midY)
                zone3 = divideAndConquer(matrix,target,startX,midY+1,midX,endY)
                zone4 = divideAndConquer(matrix, target, midX+1,midY+1,endX,endY)
                return zone2 or zone3 or zone4


        return divideAndConquer(matrix, target, 0, 0, len(matrix[0])-1, len(matrix)-1)


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3()]:
            func = Sol.searchMatrix
            self.assertEqual(func([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5), True)
            self.assertEqual(func([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20), False)
            self.assertEqual(func([[]], 1), False)
            self.assertEqual(func([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 19), True)

if __name__ == '__main__':
    unittest.main()