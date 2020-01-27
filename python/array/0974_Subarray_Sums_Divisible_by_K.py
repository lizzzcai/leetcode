'''
27/01/2020

974. Subarray Sums Divisible by K - Medium

Tag: 

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

'''

from typing import List
# Solution
class Solution1:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        '''
        https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/310767/(Python)-Concise-Explanation-and-Proof
        
        time: O(n)
        space: O(K)
        
        '''
        mod = 0
        hmap = [1] + [0] * K
        res = 0
        
        for num in A:
            mod = (mod + num) % K
            if hmap[mod]:
                res += hmap[mod]
            hmap[mod] += 1
        return res

class Solution2:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        '''
        prefix sum P[j] - [i] = sum(i, j)
        Time: O(N^2)
        Space: O(N)
        '''
        count = 0

        P = [0] * (len(A)+1)
        for i in range(len(A)):
            P[i+1] = A[i] + P[i]
        
        for i in range(len(A)+1):
            for j in range(i+1, len(A)+1):
                sum_ = P[j] - P[i]
                if sum_ % K == 0:
                    count += 1
        return count

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution1().subarraysDivByK
        self.assertEqual(func([4,5,0,-2,-3,1], 5), 7)
        self.assertEqual(func([4,5,0,-2,-3,1,4,6,8,2,3,11,4], 5), 24)

        func = Solution2().subarraysDivByK
        self.assertEqual(func([4,5,0,-2,-3,1], 5), 7)
        self.assertEqual(func([4,5,0,-2,-3,1,4,6,8,2,3,11,4], 5), 24)

if __name__ == '__main__':
    unittest.main()