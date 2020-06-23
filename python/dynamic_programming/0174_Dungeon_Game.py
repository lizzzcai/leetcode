'''
23/06/2020

174. Dungeon Game - Hard

Tag: Binary Search, Dynamic Programming

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

'''

from typing import List
import math
# Solution
class Solution1:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        https://leetcode.com/problems/dungeon-game/discuss/698271/Python-Short-DP-7-lines-O(mn)-top-down-explained
        time: O(mn)
        space: O(mn)
        '''
        if not dungeon:
            return 0
        R,C = len(dungeon), len(dungeon[0])
        
        # dp[i][j]: if we start from [i,j] to the princess cell, what is the min hp
        dp = [[math.inf] * (C+1) for _ in range(R+1)]
        
        # base case: if start from the princess cell
        dp[R-1][C] = dp[R][C-1] = 1
        
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                    # if the dungeon is positive, then we set the hp to 1
                    dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)
        
        return dp[0][0]

class Solution2:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        https://leetcode.com/problems/dungeon-game/discuss/698271/Python-Short-DP-7-lines-O(mn)-top-down-explained
        time: O(n)
        space: O(n)
        '''
        if not dungeon:
            return 0
        R,C = len(dungeon), len(dungeon[0])
        
        # dp[i][j]: if we start from [i,j] to the princess cell, what is the min hp
        dp = [math.inf] * (C)
        
        # base case: if start from the princess cell
        dp[C-1] = 1
        
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                    # if the dungeon is positive, then we set the hp to 1
                    dp[j] = max(min(dp[j:j+2]) - dungeon[i][j], 1)
        
        return dp[0]
        
            

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.calculateMinimumHP
            self.assertEqual(func([[-2,-3,3],[-5,-10,1],[10,30,-5]]),7)

if __name__ == '__main__':
    unittest.main()