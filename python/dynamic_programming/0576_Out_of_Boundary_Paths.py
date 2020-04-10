'''
11/04/2020

576. Out of Boundary Paths - Medium

Tag: Dynamic Programming

There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

 

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(N*m*n)
    Space complexity : O(m*n)
    '''
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # set up the dp, extend the grid to the boundary for easy calculation
        dp = [[0]*(n+2) for _ in range(m+2)]
        # set the begin as 1, +1 as we extend it
        dp[i+1][j+1] = 1
        # directions
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        res = 0
        # iterate at most N times
        for _ in range(N):
            dp2 = [[0]*(n+2) for _ in range(m+2)]
            for r in range(1,m+1):
                for c in range(1,n+1):
                    for dr, dc in dirs:
                        dp2[r+dr][c+dc] += dp[r][c]
            dp = dp2
        
            # at each move, sum up the number of paths to move the ball out of grid boundary
            for r in range(1, m+1):
                res += dp[r][0]
                res += dp[r][-1]
            for c in range(1, n+1):
                res += dp[0][c]
                res += dp[-1][c]

            
        return res  % (10**9 + 7)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findPaths
            self.assertEqual(func(2,2,2,0,0), 6)
            self.assertEqual(func(8,50,23,5,26), 914783380)
            self.assertEqual(func(1,3,3,0,1), 12)
            self.assertEqual(func(36,5,50,15,3), 390153306)

if __name__ == '__main__':
    unittest.main()