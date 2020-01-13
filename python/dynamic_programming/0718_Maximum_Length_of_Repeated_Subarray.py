'''
13/01/2020

718. Maximum Length of Repeated Subarray - Medium

Tag: Array, Dynamic Programming, Binary Search

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

'''

from typing import List
# Solution
class Solution:
    '''
    Time complexity : O(nm)
    Space complexity : O(nm)
    '''
    def findLength(self, A: List[int], B: List[int]) -> int:
        '''
        set dp the map of the max length of subarray apear in both array
        dp[i][j] is the longest common prefix of A[i:] and B[j:]
        When ever A[i]==B[j], we know that dp[i][j] = dp[i+1][j+1]+1
        dp with size len(A)+1, len(B)+1
        
        We can perform bottom-up dynamic programming to find the answer based on this recurrence. 
        '''
        
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        
        return max(max(row) for row in dp)

class Solution1:
    '''
    binary search

    Time Complexity: O((M+N)∗min(M,N)∗log(min(M,N)))
    where M, NM,N are the lengths of A, B. The log factor comes from the binary search. The complexity of our naive check of a given length is O((M+N)∗length), 
    as we will create the seen strings with complexity O(M∗length), then search for them with complexity O(N∗length), and our total complexity when performing our check is the addition of these two.

    Space Complexity: O(M^2), the space used by seen.

    Intuition

    If there is a length k subarray common to A and B, then there is a length j <= k subarray as well.

    Let check(length) be the answer to the question "Is there a subarray with length length, common to A and B?" This is a function with range that must take the form [True, True, ..., True, False, False, ..., False] with at least one True. We can binary search on this function.

    Algorithm

    Focusing on the binary search, our invariant is that check(hi) will always be False. We'll start with hi = min(len(A), len(B)) + 1; clearly check(hi) is False.

    Now we perform our check in the midpoint mi of lo and hi. When it is possible, then lo = mi + 1, and when it isn't, hi = mi. This maintains the invariant. At the end of our binary search, hi == lo and lo is the lowest value such that check(lo) is False, so we want lo - 1.

    As for the check itself, we can naively check whether any A[i:i+k] == B[j:j+k] using set structures.

    '''
    def findLength(self, A: List[int], B: List[int]) -> int:
        def check(length):
            seen = set(tuple(A[i:i+length]) for i in range(len(A) - length + 1))
            return any(tuple(B[j:j+length]) in seen for j in range(len(B) - length + 1))

        l, r = 0, min(len(A), len(B)) + 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
            
        return l-1

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().findLength
        self.assertEqual(func([1,2,3,2,1], [3,2,1,4,7]), 3)

        func = Solution1().findLength
        self.assertEqual(func([1,2,3,2,1], [3,2,1,4,7]), 3)

if __name__ == '__main__':
    unittest.main()