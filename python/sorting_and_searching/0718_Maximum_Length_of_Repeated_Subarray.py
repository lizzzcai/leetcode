'''
29/04/2020

718. Maximum Length of Repeated Subarray - Medium

Tag: Array, Binary Search, Dynamic Programming, Hash Table

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

class Solution1:
    def findLength(self, A: List[int], B: List[int]) -> int:
        '''
        Binary Search with Naive Check
        Time: O(O(m+n)*min(m,n)*log(min(m,n)))
        Space:O(O(m^m))
        '''

        def check(length):
            seen = set(tuple(A[i:i+length]) for i in range(len(A)-length+1))
            return any(tuple(B[j:j+length]) in seen for j in range(len(B)-length+1))

        l, r = 0, min(len(A), len(B)) + 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
            
        return r

class Solution2:
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
        


class Solution3:
    '''
    Rolling hasH + Binary search
    Time: O((m+n)*log(min(m,n)))
    Space: O(m)


    '''
    def findLength(self, A: List[int], B: List[int]) -> int:
        P, MOD = 113, 10**9 + 7
        Pinv = pow(P, MOD-2, MOD)
        def check(guess):
            def rolling(A, length):
                if length == 0:
                    yield 0, 0
                    return
                h, power = 0, 1
                for i, x in enumerate(A):
                    h = (h+x*power) % MOD
                    if i < length - 1:
                        power = (power*P) % MOD
                    else:
                        yield h, i-(length-1)
                        h = (h-A[i-(length-1)]) * Pinv % MOD
            
            hashes = collections.defaultdict(list)
            for ha, start in rolling(A, guess):
                hashes[ha].append(start)
            for ha, start in rolling(B, guess):
                iarr = hashes.get(ha, [])
                if any(A[i:i+guess] == B[start:start+guess] for i in iarr):
                    return True
            return False
                        
        l, r = 0, min(len(A), len(B)) + 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
            
        return r

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.findLength
            self.assertEqual(func([1,2,3,2,2,1], [3,2,1,4,7]), 2)

if __name__ == '__main__':
    unittest.main()