'''
01/06/2020

378. Kth Smallest Element in a Sorted Matrix - Medium

Tag: Binary Search, Heap

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(nlogn)
    Space complexity : O(1)
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
        '''
        R, C = len(matrix), len(matrix[0])
        
        l, h = matrix[0][0], matrix[R-1][C-1]
        while l <= h:
            mid = (l+h)//2
            count = 0
            j = C-1
            max_val = l
            for i in range(R):
                while j >=0 and matrix[i][j] > mid:
                    j -= 1
                if j >= 0:
                    count += j+1
                    max_val = max(max_val, matrix[i][j])
            
            if count == k:
                return max_val
            elif count < k:
                l = mid + 1
            else:
                h = mid - 1
        
        return l

import heapq
class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        if not matrix or not matrix[0]:
            return 0
        
        heap = []
        def push(i, j):
            if i < len(matrix) and j < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j], i, j))
        
        push(0, 0)
        res = matrix[0][0]
        while heap and k > 0:
            val, i, j = heapq.heappop(heap)
            res = val
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
            k -= 1
        
        return res
        


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.kthSmallest
            self.assertEqual(func([[1,5,9],[10,11,13],[12,13,15]], 8), 13)
            self.assertEqual(func([[1,2],[1,3]], 2), 1)


if __name__ == '__main__':
    unittest.main()