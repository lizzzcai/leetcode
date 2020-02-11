'''
11/02/2020

1155. Number of Dice Rolls With Target Sum - Medium

Tag: Dynamic Programming

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000

'''

from typing import List
# Solution
class Solution1:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        '''
        Runtime: O(d * f * target).
        Memory: O(d*target)
        '''
        p = 10 ** 9 + 7
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        dp[0][0] = 1
        
        for i in range(1, d+1):
            for j in range(1, target+1):
                for k in range(1,f+1):
                    if k <= j: # j-k >= 0
                        dp[i][j] += dp[i-1][j-k]
                    else:
                        break
        
        return int(dp[d][target] % p)
        
class Solution2:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        '''
        Runtime: O(d * f * target).
        Memory: O(target)
        '''
        p = 10 ** 9 + 7
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        
        for _ in range(d):
            for t in range(target, -1, -1):
                dp[t] = sum(dp[max(0, t-f):t])
        
        return int(dp[target] % p)

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().numRollsToTarget
        self.assertEqual(func(1,6,3), 1)
        self.assertEqual(func(2,6,7), 6)
        self.assertEqual(func(2,5,10), 1)
        self.assertEqual(func(1,2,3), 0)
        self.assertEqual(func(30,30,500), 222616187)

        func = Solution2().numRollsToTarget
        self.assertEqual(func(1,6,3), 1)
        self.assertEqual(func(2,6,7), 6)
        self.assertEqual(func(2,5,10), 1)
        self.assertEqual(func(1,2,3), 0)
        self.assertEqual(func(30,30,500), 222616187)


if __name__ == '__main__':
    unittest.main()