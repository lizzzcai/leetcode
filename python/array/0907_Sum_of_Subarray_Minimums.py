'''
17/05/2020

907. Sum of Subarray Minimums - Medium

Tag: Array, Stack

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000

'''

from typing import List
import collections
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(A)
        
        # prev has i*-1 in increasing order of A[i*-1]
        # where i* is the answer to query j
        stack = []
        prev = [None] * N
        for i in range(N):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        # next has k* + 1 in increasing order of A[k*+1]
        # where k* is the answer to query j
        stack = []
        nxt = [None] * N
        for k in range(N-1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            nxt[k] = stack[-1] if stack else N
            stack.append(k)

        return sum((i-prev[i])*(nxt[i]-i)*A[i] for i in range(N))%MOD

class Solution2:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(A)
        
        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # add all answers for subarrays [i,j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x*c
            
            stack.append((y, count))
            dot += y * count
            ans += dot
        
        return ans % MOD

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.sumSubarrayMins
            self.assertEqual(func([3,1,2,4]), 17)
            self.assertEqual(func([3,1,2,4,6,4,2,1,7]), 82)
            self.assertEqual(func([85]), 85)


if __name__ == '__main__':
    unittest.main()