'''
27/05/2020

1074. Number of Submatrices That Sum to Target - Hard

Tag: Array, Dynamic Programming, Sliding Windows

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
 

Note:

1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8


'''

from typing import List
import collections
# Solution
class Solution1:

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        '''
        https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750/JavaC%2B%2BPython-Find-the-Subarray-with-Target-Sum
        
        2-d prefix sum
        Time O(mn^2)
        Space O(mn)
        
        '''
        P = []
        for row in matrix:
            p = [0]
            for x in row:
                p.append(p[-1]+x)
            P.append(p)

        res = 0
        for c1 in range(len(P[0])):
            for c2 in range(c1+1, len(P[0])):
                count = collections.defaultdict(int)
                cur_sum = 0
                count[0] = 1
                for r in range(len(P)):
                    cur_sum += (P[r][c2] - P[r][c1])
                    res += count[cur_sum - target] # target = curr_sum - prev
                    count[cur_sum] += 1
        
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
            func = Sol.numSubmatrixSumTarget
            self.assertEqual(func([[0,1,0],[1,1,1],[0,1,0]], 0), 4)
            self.assertEqual(func([[1,-1],[-1,1]], 0), 5)



if __name__ == '__main__':
    unittest.main()