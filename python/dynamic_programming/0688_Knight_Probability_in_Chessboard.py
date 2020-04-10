'''
10/04/2020

688. Knight Probability in Chessboard - Medium

Tag: Dynamic Programming

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

 



 

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 

Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n^2K)
    Space complexity : O(n^2)
    '''
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in dirs:
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
        
            dp = dp2
        
        return sum(map(sum, dp))

class Solution2:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        def helper(memo, N, K, r, c):
            if K == 0:
                return 1
            
            out = 0
            for dr, dc in dirs:
                if 0 <= r + dr < N and 0 <= c + dc < N:
                    if (K,r+dr,c+dc) not in memo:
                        memo[(K,r+dr,c+dc)] = helper(memo, N, K-1, r + dr, c + dc)
                    out += memo[(K,r+dr,c+dc)]

            return out  / 8.0
        
        
        memo = {}
        dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        return helper(memo, N, K, r, c)


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.knightProbability
            self.assertEqual(func(3,2,0,0), 0.06250)
            self.assertAlmostEqual(func(3,3,0,0), 0.01562, 5)

if __name__ == '__main__':
    unittest.main()