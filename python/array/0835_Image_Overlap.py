'''
07/09/2020

835. Image Overlap - Medium

Tag: Array

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
'''

from typing import List
import collections
# Solution


class Solution1:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def shift_and_count(x_shift, y_shift, M, R):
            """ 
                Shift the matrix M, and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up and left is equivalent to
                moving the other matrix down and right
            """
            count = 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        count += 1
            return count

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                max_overlaps = max(max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        return max_overlaps

class Solution2:

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        '''
        Time: O(N^4)
        Space: O(N^2)
        
        '''
        dim = len(A)

        def non_zero_cells(M):
            res = []
            for x in range(dim):
                for y in range(dim):
                    if M[x][y] == 1:
                        res.append((x,y))
            return res
        
        count = collections.defaultdict(int)
        max_overlaps = 0
        
        A_ones = non_zero_cells(A)
        B_ones = non_zero_cells(B)
        
        for (x_a, y_a) in A_ones:
            for (x_b, y_b) in B_ones:
                vec = (x_b-x_a, y_b-y_a)
                count[vec] += 1
                max_overlaps = max(max_overlaps, count[vec])
                
        return max_overlaps

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.largestOverlap
            A = [[1,1,0],[0,1,0],[0,1,0]]
            B = [[0,0,0],[0,1,1],[0,0,1]]

            self.assertEqual(func(A,B), 3)

if __name__ == '__main__':
    unittest.main()