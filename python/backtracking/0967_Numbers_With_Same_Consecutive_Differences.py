'''
18/08/2020

967. Numbers With Same Consecutive Differences - Medium

Tag: Backtracking, Dynamic Programming

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9


'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(10*2^(N-1))
    Space complexity : O(10*2^(N-1))
    '''
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
        if N == 1:
            return [x for x in range(10)]
        
        def backtracking(i, track, N, K):
            if i == N-1:
                res.append(track)
                return
            
            last = track % 10
            for k in set([-K, K]):
                nxt = last + k
                if 0<=nxt<10:
                    backtracking(i+1, track*10 + nxt, N, K)
        
        res = []
        
        for i in range(1, 10):
            backtracking(0, i, N, K)
        
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.numsSameConsecDiff
            self.assertEqual(func(3,7), [181,292,707,818,929])
            self.assertEqual(func(1,4), [0,1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main()