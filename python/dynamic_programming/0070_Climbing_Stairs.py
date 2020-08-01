'''
01/08/2020

70. Climbing Stairs - Easy

Tag: Dynamic Programming

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]
            
        
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.climbStairs
            self.assertEqual(func(1), 1)
            self.assertEqual(func(2), 2)
            self.assertEqual(func(3), 3)
            self.assertEqual(func(4), 5)
            self.assertEqual(func(5), 8)



if __name__ == '__main__':
    unittest.main()