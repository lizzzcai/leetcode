'''
08/02/2020

221. Maximal Square - Medium

Tag: Dynamic Programming

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

'''

from typing import List
# Solution
class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        # Brute Force
        Time: O((mn)^2)
        Space:O(1)
        '''
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        max_len = 0
        # iterate one by one
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    # start from this cell and increase the len
                    len_ = 1
                    is_sqrt = True
                    while r+len_ < rows and c+len_ < cols and is_sqrt:
                        #check row by row
                        for k in range(r, r+len_+1):
                            if matrix[k][c+len_] == '0':
                                is_sqrt = False
                                break
                        
                        # check col by col
                        for k in range(c, c+len_+1):
                            if matrix[r+len_][k] == "0":
                                is_sqrt = False
                                break
                        
                        if is_sqrt:
                            len_ += 1
                        
                    max_len = max(max_len, len_)
        
        return max_len * max_len

class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        Dynamic Programmming
        Time O(mn)
        SpaceO(mn)
        '''
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        # init the dp
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        max_len = 0
        
        # fill the first row and first col
        for r in range(rows):
            if matrix[r][0] == "1":
                dp[r][0] = 1
                max_len = 1
        for c in range(cols):
            if matrix[0][c] == "1":
                dp[0][c] = 1
                max_len = 1
        
        # dp the rest
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
                    max_len = max(max_len, dp[r][c])
        
        return max_len * max_len

class Solution3:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        Dynamic Programmming
        Time O(mn)
        SpaceO(n)
        '''
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        # init the dp
        dp = [0 for _ in range(cols+1)]
        max_len = 0
        prev = 0
        
        # fill the first col
        for c in range(1, cols+1):
            if matrix[0][c-1] == "1":
                dp[c] = 1
                max_len = 1
        
        # dp the rest
        for r in range(2, rows+1):
            for c in range(1, cols+1):
                tmp = dp[c]
                if matrix[r-1][c-1] == "1":
                    dp[c] = min(dp[c], prev, dp[c-1]) + 1
                    max_len = max(max_len, dp[c])
                else:
                    dp[c] = 0
                prev = tmp
                
        return max_len * max_len

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().maximalSquare
        self.assertEqual(func([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 4)
        self.assertEqual(func([["1","1"]]), 1)

        func = Solution2().maximalSquare
        self.assertEqual(func([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 4)
        self.assertEqual(func([["1","1"]]), 1)

        func = Solution3().maximalSquare
        self.assertEqual(func([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 4)
        self.assertEqual(func([["1","1"]]), 1)


if __name__ == '__main__':
    unittest.main()