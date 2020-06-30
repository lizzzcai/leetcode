'''
27/06/2020

279. Perfect Squares - Medium

Tag: Math, Dynamic Programming, Breath-first Search

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n^2)
    Space complexity : O(n)
    '''
    def numSquares(self, n: int) -> int:
        #dp[i] is the least number of perfect square numbers for i
        dp = [n]*(n+1)
        # base case
        dp[0] = 0
        
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        
        return dp[n]

class Solution2:
    def numSquares(self, n: int) -> int:
        '''
        BFS
        '''
        
        pef_sqr = []
        i = 1
        while i*i <= n:
            pef_sqr.append(i*i)
            i+=1
        
        if pef_sqr[-1] == n:
            return 1
        
        ans = 0
        check = set([n])
        while check:
            ans += 1
            tmp = set()
            for x in check:
                for y in pef_sqr:
                    if x == y:
                        return ans
                    if x < y:
                        break
                    tmp.add(x-y)
            
            check = tmp
        
        return ans

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2()]:
            func = Sol.numSquares
            self.assertEqual(func(12), 3)
            self.assertEqual(func(13), 2)


if __name__ == '__main__':
    unittest.main()