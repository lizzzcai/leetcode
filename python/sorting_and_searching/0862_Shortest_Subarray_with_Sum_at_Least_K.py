'''
21/04/2020

862. Shortest Subarray with Sum at Least K - Hard

Tag: Binary Search, Queue, Sliding Window

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

'''

from typing import List
import collections

# Solution
class Solution1:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        '''
        Sliding windows
        Time O(N)
        Space O(N)
        
        '''
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        
        # we are looking for smallest y-x so that Py-Px >= K
        ans = N+1
        # opt(y) candidates, representeed as indices of P
        monoq = collections.deque()
        for y, Py in enumerate(P):
            # want opt(y) = largest x with Px <= Py - K
            '''
            If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1, as if P[x1] <= P[y] - K,
            then P[x2] <= P[x1] <= P[y] - K but y - x2 is smaller.
            This implies that our candidates x for opt(y) will have increasing values of P[x].
            
            in this case, we can just pop out x1 and keep x2
            '''
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()
            
            while monoq and Py - P[monoq[0]] >= K: # Py >= P[x] + K
                ans = min(ans, y - monoq.popleft())
            
            monoq.append(y)
            
        return ans if ans < N+1 else -1   




# Solution
class Solution2:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        '''
        Sliding windows
        Time O(N)
        Space O(N)

        compute prefix sum on the fly
        
        '''
        N = len(A)
        curr_sum = 0
        # we are looking for smallest y-x so that Py-Px >= K
        ans = N+1
        # opt(y) candidates, representeed as indices of P
        monoq = collections.deque([(0,0)])
        for idx, x in enumerate(A):
            # want opt(y) = largest x with Px <= Py - K
            '''
            If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1, as if P[x1] <= P[y] - K, then P[x2] <= P[x1] <= P[y] - K but y - x2 is smaller.
            This implies that our candidates x for opt(y) will have increasing values of P[x].
            
            in this case, we can just pop out x1 and keep x2
            '''
            curr_sum += x
            while monoq and curr_sum - monoq[0][1] >= K: # Py >= P[x] + K
                ans = min(ans, idx - monoq.popleft()[0]+1)
                
            while monoq and curr_sum <= monoq[-1][1]:
                monoq.pop()
            
            monoq.append((idx+1, curr_sum))
            
        return ans if ans < N+1 else -1   


import heapq
class Solution3:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        '''
        Heap
        Time O(NlogN)
        Space O(N)
        
        '''
        N = len(A)
        res = N + 1
        curr_sum = 0
        heap = []
        for idx, x in enumerate(A):
            curr_sum += x
            if curr_sum >= K:
                res = min(res, idx+1)
            
            while heap and curr_sum - heap[0][0] >= K:
                res = min(res, idx - heapq.heappop(heap)[1]+1)
            
            heapq.heappush(heap, (curr_sum, idx+1))
        
        return res if res < N+1 else -1


class Solution4:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        '''
        mono stack + binary search

        Time O(NlogN)
        Space: O(N)
        '''
        N = len(A)
        res = N + 1
        curr_sum = 0
        stack = [(0,0)]
        
        for idx, x in enumerate(A):
            curr_sum += x
            while stack and curr_sum <= stack[-1][0]:
                stack.pop()
            
            stack.append((curr_sum, idx+1))
            i = self.binarysearch(stack, curr_sum - K)
            if i >= 0:
                res = min(res, idx-stack[i][1]+1)
            
        
        return res if res < N+1 else -1
    
    def binarysearch(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return right



# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2(), Solution3(), Solution4()]:
            func = Sol.shortestSubarray
            self.assertEqual(func([1], 1), 1)
            self.assertEqual(func([1,2], 4), -1)
            self.assertEqual(func([77,19,35,10,-14],19), 1)
            self.assertEqual(func([84,-37,32,40,95], 167), 3)

if __name__ == '__main__':
    unittest.main()