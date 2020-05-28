'''
27/05/2020

363. Max Sum of Rectangle No Larger Than K - Hard

Tag: Binary Search, Dynamic Programming, Queue

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?


'''

from typing import List
import collections
import math
import bisect
# Solution
class Solution1:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        P = []
        for row in matrix:
            p = [0]
            for x in row:
                p.append(p[-1]+x)
            P.append(p)
        
        res = -math.inf
        for c1 in range(len(P[0])):
            for c2 in range(c1+1, len(P[0])):
                # 2-D prefix sum between c1 and c2
                curr_sum, curr_P = 0, [0]
                for r in range(len(P)):
                    curr_sum += P[r][c2]-P[r][c1]
                    idx = bisect.bisect_left(curr_P, curr_sum - k)
                    if idx < len(curr_P):
                        res = max(res, curr_sum - curr_P[idx])
                        if res == k:
                            return res
                    bisect.insort_left(curr_P, curr_sum)
        
        return res


class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        P = []
        for row in matrix:
            p = [0]
            for x in row:
                p.append(p[-1]+x)
            P.append(p)
        
        res = -math.inf
        for c1 in range(len(P[0])):
            for c2 in range(c1+1, len(P[0])):
                # 2-D prefix sum between c1 and c2
                curr_sum, curr_P = 0, [0]
                for r in range(len(P)):
                    curr_sum += P[r][c2]-P[r][c1]
                    idx = bisect.bisect_left(curr_P, curr_sum - k)
                    if idx < len(curr_P):
                        res = max(res, curr_sum - curr_P[idx])
                        if res == k:
                            return res
                    bisect.insort_left(curr_P, curr_sum)
        
        return res 
    


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.maxSumSubmatrix
            self.assertEqual(func([[1,0,1],[0,-2,3]], 2), 2)
            self.assertEqual(func([[2,2,-1]], 0), -1)
            self.assertEqual(func([[-9,-6,-1,-7,-6,-5,-4,-7,-6,0],[-4,-9,-4,-7,-7,-4,-4,-6,-6,-6],[-2,-2,-6,-7,-7,0,-1,-1,-8,-2],[-5,-3,-1,-6,-1,-1,-6,-3,-4,-8],[-4,-1,0,-8,0,-9,-8,-7,-2,-4],[0,-3,-1,-7,-2,-5,-5,-5,-8,-7],[-2,0,-8,-2,-9,-2,0,0,-9,-6],[-3,-4,-3,-7,-2,-1,-9,-5,-7,-2],[-8,-3,-2,-8,-9,0,-7,-8,-9,-3],[-7,-4,-3,-3,-3,-1,0,-1,-8,-2]], -321), -323)



if __name__ == '__main__':
    unittest.main()