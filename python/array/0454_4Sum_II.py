"""
19/09/2019
454. 4Sum II - Medium
Tag: Array


Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^23 - 1.


Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

"""

from typing import List
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        time: O(n^2)
        space: O(n^2)
        """
        # init count map
        cnt = {}
        for a in A:
            for b in B:
                s = a + b
                # count the number of a+b
                cnt[s] = cnt.get(s, 0) + 1
        
        res = 0
        for c in C:
            for d in D:
                # cal the -(c + d)
                t = - c - d
                # check if t in cnt, so a + b = -(c + d), a+b+c+d = 0
                if t in cnt:
                    res += cnt[t]
                
        return res
        
        

# Unit Test
import unittest
class fourSumCountCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fourSumCount(self):
        func = Solution().fourSumCount
 

        self.assertEqual(func(
            [1,2], [-2,-1], [-1,2], [0,2]
                            ), 2)






if __name__ == '__main__':
    unittest.main()


