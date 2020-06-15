'''
14/06/2020
786. K-th Smallest Prime Fraction - Hard

Tag: Binary Search, Heap

A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]
Note:

A will have length between 2 and 2000.
Each A[i] will be between 1 and 30000.
K will be between 1 and A.length * (A.length - 1) / 2.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(nlogn^2)
    Space complexity : O(1)
    '''
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        '''

           5   3   2  1
        1 1/5 1/3 1/2 1
        2 2/5 2/3  1  2
        3 3/5  1  3/2 3
        5  1  5/3 2/5 5

        increase from left to right
        increase from top to bottom
        
        https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378
        
        (n * log(MAX^2)), where MAX is the maximum element in A
        Space complexity: O(1)
        
        '''
        
        m = len(A)
        l, h = 0, 1
        p, q = 0, 1
        
        while l < h:
            mid = (l+h) / 2.0
            count = 0
            j = m-1
            p = 0
            for i in range(m):
                while j >= 0 and A[i] > mid*A[m-j-1]: 
                    j -= 1
                if j >= 0:
                    count += j+1
                    if A[m-j-1]*p < A[i]*q: # A[i]/A[m-j-i]>p/q
                        p,q = A[i], A[m-j-1]
            
            if count == K:
                return [p, q]
            elif count < K:
                l = mid
            else:
                h = mid

import heapq
class Solution2:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        '''
           5   3   2  1
        1 1/5 1/3 1/2 1
        2 2/5 2/3  1  2
        3 3/5  1  3/2 3
        5  1  5/3 2/5 5

        increase from left to right
        increase from top to bottom
        
        https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378
        
        Time complexity: O(K * log(k) with n = A.length
        Space complexity: O(n)
        
        '''
        heap = []
        
        def push(i, j):
            if i < len(A) and j < len(A):
                heapq.heappush(heap, (A[i]/A[len(A)-j-1], i, j))
        
        push(0, 0)
        res = [1, 1]
        while heap and K > 0:
            fra, i, j = heapq.heappop(heap)
            res = [A[i], A[len(A)-j-1]]
            push(i, j+1)
            if j == 0:
                push(i+1, j)
            
            K -= 1
            
        return res


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.kthSmallestPrimeFraction
            self.assertEqual(func([1, 2, 3, 5], 3), [2,5])
            self.assertEqual(func([1,13,17,59], 6), [13,17])


if __name__ == '__main__':
    unittest.main()