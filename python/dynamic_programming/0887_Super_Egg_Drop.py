'''
03/06/2020

887. Super Egg Drop - Hard

Tag: Dynamic Programming, Binary Search, Math

You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000

'''

from typing import List
# Solution
class Solution1:
    def superEggDrop(self, K: int, N: int) -> int:
        '''
        https://juejin.im/post/5d9ede57518825358b221349
        
        Time O(KNlogN)
        Space O(KN)
        '''
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    while lo+1< hi:
                        x = (lo+hi)//2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)
                        
                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                
                    ans = 1 + min((max(dp(k-1, x-1), dp(k, n-x)) for x in (lo, hi)))
                    
                memo[k, n] = ans
            return memo[k, n]
        
        return dp(K, N)



class Solution2:
    def superEggDrop(self, K: int, N: int) -> int:
        '''
        https://juejin.im/post/5d9ede57518825358b221349
        https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)
        Time O(KlogN)
        Space O(KN)
        
        The key concept of the original O(KN^2) solution is to try all the floor to get the min-cost min(max(broke, not broke) for every floor) as the answer.

        Original DP definition: I stand on nth floor and give me k eggs, the minimum times I try is dp[n][k]. This definition means the result of this problem is dp[N][K].

        This solution is somehow a reverse thinking:

        New DP definition: If you give me k egg, let me drop m times, I can try out maximum dp[m][k] floors. Based on this definition, the result is some m, which cases dp[m][K] equals N.

        The transfer equation is based on the following facts:

        No matter which floor you try, the egg will only break or not break, if break, go downstairs, if not break, go upstairs.

        No matter you go up or go down, the num of all the floors is always upstairs + downstairs + the floor you try, which is dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1.
        
        '''
        dp = [[0]*(K+1) for _ in range(N+1)]
        for m in range(1, N+1):
            for n in range(1, K+1):
                dp[m][n] = dp[m-1][n-1] + dp[m-1][n] + 1
                if dp[m][n] >= N:
                    return m
                
        return dp[N][K]

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.superEggDrop
            self.assertEqual(func(2, 6), 3)
            self.assertEqual(func(3, 14), 4)
            self.assertEqual(func(1,2), 2)
            self.assertEqual(func(3, 25), 5)




if __name__ == '__main__':
    unittest.main()