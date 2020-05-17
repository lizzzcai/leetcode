'''
16/05/2020

918. Maximum Sum Circular Subarray - Medium

Tag: Array

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 

Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
'''

from typing import List
import collections
# Solution
class Solution1:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        '''
        Time O(N)
        Space O(N)
        
        '''
        N = len(A)
        
        P = [0]
        for _ in range(2):
            for x in A:
                P.append(P[-1]+x)
        
        ans = A[0]
        q = collections.deque([0])
        for j in range(1, len(P)):
            # j-N <= i < j
            if q[0] < j-N:
                q.popleft()
            
            # the optimal i is deque[0] for cand. answer = P[j] - P[i]
            ans = max(ans, P[j] - P[q[0]])

            # remove any i1 with [i2] <= P[i1]
            while q and P[q[-1]] >= P[j]:
                q.pop()
            
            q.append(j)

            
        return ans


class Solution2:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        '''
        Time O(N)
        Space O(1)
        
        '''
        def kadane(gen):
            ans = cur = -math.inf
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans
        
        S = sum(A)
        ans1 = kadane(A)
        ans2 = S + kadane([-x for x in A[1:]])
        ans3 = S + kadane([-x for x in A[:-1]])
        
        return max(ans1,ans2,ans3)

import math
class Solution3:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        '''
        Time O(N)
        Space O(1)
        
        '''
        S = sum(A)
        # ans1: answer for one0interval subarray
        ans1 = cur = -math.inf
        for x in A:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)
        
        # ans2: answer for two-interval subarray, interior in A[1:]
        ans2 = cur = math.inf
        for i in range(1, len(A)):
            cur = A[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = S - ans2
        
        # ans3: answer for two0interval subarray, interior in A[:-1]
        ans3 = cur = math.inf
        for i in range(0, len(A)-1):
            cur = A[i] + min(cur, 0)
            ans3 = min(ans3, cur)
        ans3 = S - ans3
        
        return max(ans1, ans2, ans3)     

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(),Solution2(), Solution3()]:
            func = Sol.maxSubarraySumCircular
            self.assertEqual(func([1,-2,3,-2]), 3)
            self.assertEqual(func([5,-3,5]), 10)
            self.assertEqual(func([3,-1,2,-1]), 4)
            self.assertEqual(func([3,-2,2,-3]), 3)
            self.assertEqual(func([-2,-3,-1]), -1)
            self.assertEqual(func([1,2,3]), 6)
            self.assertEqual(func([1,2,2,2,1]), 8)
            self.assertEqual(func([6,9,-3]), 15)


if __name__ == '__main__':
    unittest.main()