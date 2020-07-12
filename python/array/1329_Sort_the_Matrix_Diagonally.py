'''
12/07/2020

1329. Sort the Matrix Diagonally - Medium

Tag: Array, Sort

Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100

'''

from typing import List
import collections
# Solution
class Solution1:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        for element in the same diag, i-j is the same
        collect all the elements for each i-j, then sort them seperately and put it back
        
        Time: O(MNlogD) D=MIN(m,n)
        Space: O(mn)
        
        https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/489749/JavaPython-Straight-Forward
        '''
        diags = collections.defaultdict(list)
        R, C = len(mat), len(mat[0])
        # get all the i-j into diags
        for i in range(R):
            for j in range(C):
                diags[i-j].append(mat[i][j])
        # sort it reversely for easy pop out
        for k in diags:
            diags[k].sort(reverse=True)
        
        # put it back
        for i in range(R):
            for j in range(C):
                mat[i][j] = diags[i-j].pop()
        
        return mat
            
        

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.diagonalSort
            self.assertEqual(func([[3,3,1,1],[2,2,1,2],[1,1,1,2]]), [[1,1,1,1],[1,2,2,2],[1,2,3,3]])

if __name__ == '__main__':
    unittest.main()